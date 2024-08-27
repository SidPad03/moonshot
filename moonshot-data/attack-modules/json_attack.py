import os
import json
from moonshot.src.redteaming.attack.attack_module import AttackModule
from moonshot.src.redteaming.attack.attack_module_arguments import AttackModuleArguments

class JSONAttackModule(AttackModule):
    def __init__(self, am_id: str, am_arguments: AttackModuleArguments | None = None):
        super().__init__(am_id, am_arguments)
        self.name = "JSON Attack Module"
        self.description = "This custom attack module loads prompts from a data path. Please provide a path to a directory containing JSON files as the initial prompt."

    def get_metadata(self) -> dict:
        """
        Get metadata for the attack module.

        Returns a dictionary containing the id, name, and description of the attack module. If the name or description
        is not available, empty strings are returned.

        Returns:
            dict | None: A dictionary containing the metadata of the attack module, or None if the metadata is not
            available.
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description if hasattr(self, "description") else "",
        }

    async def execute(self):
        """
        Asynchronously executes the attack module.

        This method loads the dataset contents using the `load_dataset_contents` method,
        processes the dataset through a prompt template, retrieves the connector to the first
        Language Learning Model (LLM) and sends the processed dataset as a prompt to the LLM.
        """
        self.load_modules()
        return await self.perform_attack_manually()

    async def perform_attack_manually(self) -> list:
        """
        Asynchronously performs the attack manually. The user will need to pass in a list of prompts and
        the LLM connector endpoint to send the prompts to. In this example, there is a for loop to send the
        list of prepared prompts to all the LLM connectors defined.

        This method prepares prompts for each target Language Learning Model (LLM) using the provided prompt
        and sends them to the respective LLMs.
        """
        data = self.load_json_from_dir()

        result_list = []
        prompt_list = []

        for prompt in data:
            prompt_list.append(prompt)

        result_list.append(
            await self._send_prompt_to_all_llm(
                prompt_list
            )
        )

        return result_list

    def load_json_from_dir(self):
        prompts_dict = {}

        for root, dirs, files in os.walk(self.prompt):
            json_files = [file for file in files if file.endswith('.json')]
            for json_file in json_files:
                file_path = os.path.join(root, json_file)
                try:
                    with open(file_path, 'r') as file:
                        data = json.load(file)
                        if 'prompts' in data:
                            prompts_dict.update(data['prompts'])
                except (IOError, json.JSONDecodeError) as e:
                    print(f"Error reading or parsing file {file_path}: {e}")

        return prompts_dict