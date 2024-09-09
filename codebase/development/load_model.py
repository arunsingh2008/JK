

import json
from transformers import AutoModelForCausalLM, AutoTokenizer

class Llama3Model:
    def __init__(self, config_path):
        with open(config_path, 'r') as config_file:
            self.config = json.load(config_file)
        self.model = AutoModelForCausalLM.from_pretrained(self.config['model_path'])
        self.tokenizer = AutoTokenizer.from_pretrained(self.config['model_path'])

    def generate_text(self, prompt):
        input_ids = self.tokenizer.encode(prompt, return_tensors='pt')
        output = self.model.generate(input_ids, max_length=self.config['max_tokens'], temperature=self.config['temperature'], top_p=self.config['top_p'])
        return self.tokenizer.decode(output[0], skip_special_tokens=True)

if __name__ == '__main__':
    model = Llama3Model('model_config.json')
    prompt = 'Hello, world!'
    print(model.generate_text(prompt))

