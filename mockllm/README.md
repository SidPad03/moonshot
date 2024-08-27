# Fake LLM using Flask

> Flask: A micro web service framwork using python. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.

- **Mimics OpenAI’s API**: Fake LLM simulates responses from an AI model based on predefined inputs and outputs, structured to mirror what might be expected from a real OpenAI API call.

### Using Fake LLM on moonshot

```bash
# Add fake llm as endpoint using openai-connector
add_endpoint openai-connector 'Fake LLM' http://localhost:5001/v1/ ollama 10 1 "{'model': 'fakellm'}"

# Create session with fake LLM
new_session test-fake-llm -e "['fake-llm']"
```

### Running Fake LLM Flask Application

```python
# Run with python
# Path flag is the path to the directory of json files. 

python app.py --path="data"
```

#### Example of data prompt-response data directory

```bash
data
├── dev0
│   └── data.json
├── dev1
│   ├── data2.json
│   └── devA
│       └── data3.json
└── dev2
    ├── devA
    │   ├── data4.json
    │   └── devI
    │       └── data6.json
    └── devB
        └── data5.json

# Here you can think of each subfolder containing prompt-response pairs from different categories such as prompt-injection, mailcious-question, etc.
```

### Sturcture of prompt-response JSON object file

```json
{
  "prompts": {
    // List all prompt-response pairs in the format as shown below
    "prompt1": "response1",
    "prompt2": "response2",
    "prompt3": "response3",
    ...etc
  }
}
```
