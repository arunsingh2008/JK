


from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

def setup_ai_model():
    model_name = 'allenai/led-large-16384-arxiv'
    # Download Llama3 model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    # Test model with sample input
    sample_input = 'This is a test input for the Llama3 model.'
    inputs = tokenizer.encode('summarize: ' + sample_input, return_tensors='pt', max_length=512, truncation=True)
    outputs = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Confirm model is ready for use
    print('Model is ready for use. Summary for test input:', summary)

if __name__ == '__main__':
    setup_ai_model()



