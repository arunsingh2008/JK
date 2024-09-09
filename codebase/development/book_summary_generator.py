


import openai
import requests

class BookSummaryGenerator:
    def __init__(self, openai_api_key, book_content_url):
        self.openai_api_key = openai_api_key
        self.book_content_url = book_content_url

    def fetch_book_content(self):
        response = requests.get(self.book_content_url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception('Failed to fetch book content')

    def generate_summary(self, book_content):
        openai.api_key = self.openai_api_key
        response = openai.Completion.create(
          engine="text-davinci-003",
          prompt="Summarize this book: \n\n" + book_content,
          temperature=0.7,
          max_tokens=150,
          top_p=1.0,
          frequency_penalty=0.0,
          presence_penalty=0.0
        )
        return response.choices[0].text.strip()

    def get_book_summary(self):
        book_content = self.fetch_book_content()
        summary = self.generate_summary(book_content)
        return summary



