import os
import json
import time
import logging
import argparse
import asyncio

from quart import Quart, request, jsonify, stream_with_context, Response

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Quart(__name__)

parser = argparse.ArgumentParser(description='Run the Quart app with a data directory.')
parser.add_argument('--path', type=str, help='Directory path to load data from', required=True)
args = parser.parse_args()

directory_path = args.path


def load_data_recursive(directory_path):
    """
    Recursively loads JSON data from files in the specified directory path.

    Args:
        directory_path (str): The path to the directory from which to load JSON files.

    Returns:
        list: A list of dictionaries, where each dictionary is the content of one JSON file.
    """
    json_data = []

    for root, dirs, files in os.walk(directory_path):
        json_files = [file for file in files if file.endswith('.json')]
        for json_file in json_files:
            file_path = os.path.join(root, json_file)
            with open(file_path, 'r') as f:
                data = json.load(f)
                json_data.append(data)

    return json_data


def load_responses(directory_path):
    """
    Loads and aggregates responses from JSON files in the specified directory, assuming these files contain "prompts" fields.

    Args:
        directory_path (str): The path to the directory from which to load response data.

    Returns:
        dict: A dictionary where keys are prompts and values are corresponding responses.
    """
    all_json_data = load_data_recursive(directory_path)
    responses_dict = {}
    for data in all_json_data:
        if 'prompts' in data:
            responses_dict.update(data['prompts'])
    return responses_dict


# Load responses from a specified directory path
responses = load_responses(directory_path)


@app.route('/v1/chat/completions', methods=['POST'])
async def chat_completions():
    """
    Handles incoming POST requests that contain user messages, fetches appropriate responses, finds optional parameters list, and streams them back based on flag.

    Returns:
        Response: A Quart response object that streams generated responses as server-sent events (SSE).
    """
    request_data = await request.get_json()
    logging.info(f'Received request data: {request_data}')

    prompt = ""
    if 'messages' in request_data:
        for message in request_data['messages']:
            if message['role'] == 'user':
                prompt = message['content']
                break

    logging.info(f'Handling prompt: {prompt}')

    optional_params = prompt.split()[0]
    logging.info(f'Loaded optional parameters: {optional_params}')

    response_content = responses.get(prompt, "Sorry, I do not have a response for that.")
    logging.info(f'Found response content: {response_content}')

    try:
        list_of_params = optional_params.split(":")

        attack_family = list_of_params[0]
        logging.info(f'Attack family set to {attack_family}.')

        test_number = int(list_of_params[1])
        logging.info(f'Test number set to {test_number}.')

        stream_value = list_of_params[2].split("=")[1]
        logging.info(f'Stream value set to {stream_value}.')
        if stream_value == "true":
            mimic_type = list_of_params[3].split("=")[1]
            logging.info(f'Mimic type set to {mimic_type}')
    except Exception as e:
        print("An error occurred:", str(e))

    if stream_value == "true":
        logging.info(f'Starting streaming service.')
        # Split the response_content string and include spaces in list.
        words_api = [i for j in response_content.split() for i in (j, ' ')][:-1]
        words_web = response_content.split()

        async def generate_response():
            """
           Asynchronously generates and streams response chunks. Each chunk contains a part of the response message,
           formatted for Server-Sent Events (SSE). This function simulates a delay between sending each word to mimic
           a real-time streaming effect.

           Yields:
               str: A formatted string representing a JSON object, each representing a part of the final response,
                    suitable for SSE. The string is prefixed with 'data:' to comply with SSE format.
           """
            # Iterate over words to simulate generating multiple chunks
            if mimic_type == "api":
                for i, word in enumerate(words_api):
                    chunk = {
                        "id": f"chatcmpl-mockstream-{i}",
                        "choices": [{
                            "delta": {
                                "content": word,
                                "function_call": None,
                                "role": "assistant",
                                "tool_calls": None
                            },
                            "finish_reason": None if i < len(words_api) - 1 else "end_of_stream",
                            "index": 0,
                            "logprobs": None
                        }],
                        "created": int(time.time()),
                        "model": "custom-model",
                        "object": "chat.completion.chunk",
                        "system_fingerprint": "fp_api",
                        "usage": None
                    }
                    # Format the chunk as a JSON string and prepend with "data:" for SSE
                    yield f'data: {json.dumps(chunk)}\n\n'
                    await asyncio.sleep(0.3)  # Simulate delay between chunks
            else:
                sentence = ""
                for i, word in enumerate(words_web):
                    sentence += (word + " ")
                    chunk = {
                        "id": f"chatcmpl-mockstream-{i}",
                        "choices": [{
                            "delta": {
                                "content": sentence if i < len(words_web) - 1 else sentence[:len(sentence) - 1],
                                "function_call": None,
                                "role": "assistant",
                                "tool_calls": None
                            },
                            "finish_reason": None if i < len(words_web) - 1 else "end_of_stream",
                            "index": 0,
                            "logprobs": None
                        }],
                        "created": int(time.time()),
                        "model": "custom-model",
                        "object": "chat.completion.chunk",
                        "system_fingerprint": "fp_web",
                        "usage": None
                    }
                    # Format the chunk as a JSON string and prepend with "data:" for SSE
                    yield f'data: {json.dumps(chunk)}\n\n'
                    await asyncio.sleep(0.3)  # Simulate delay between chunks

        return Response(generate_response(), mimetype='text/event-stream')
    else:
        """
        Handle POST requests by extracting prompts from the request data,
        finding the corresponding response, and returning it as a JSON.
    
        Args:
            None, operates on the incoming request.
    
        Returns:
            JSON response containing the appropriate chat completion.
        """
        logging.info(f'Starting non-streaming service.')
        # Structure the response and send
        response = {
            "choices": [
                {
                    "message": {
                        "content": response_content
                    }
                }
            ]
        }

        logging.info(f'Sending structured response: {response}')
        return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
