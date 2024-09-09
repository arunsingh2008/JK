


import requests

def generate_summary_with_llama3(aggregated_text):
    # Assuming there's an API endpoint for Llama3 model
    LLAMA3_API_URL = 'https://api.llama3.example.com/generate-summary'
    response = requests.post(LLAMA3_API_URL, json={'text': aggregated_text})
    if response.status_code == 200:
        return response.json().get('summary', '')
    else:
        return 'Error generating summary'


