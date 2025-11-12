import wikipediaapi
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
wiki_wiki = wikipediaapi.Wikipedia('CompanyResearcher', 'en', extract_format=wikipediaapi.ExtractFormat.WIKI)

def get_wikipedia_page_summary(page_title):
    page = wiki_wiki.page(page_title)
    if page.exists():
        return page.summary
    else:
        return "Page not found."
    
def get_openai_response(user_input):
    wiki_info = get_wikipedia_page_summary(user_input)
    if wiki_info:
        prompt = f"Based on the following information from Wikipedia: '{wiki_info}', answer the question: '{user_input}'"
    else:
        prompt = f"Answer the question: '{user_input}'"

    response = openai.chat.completions.create(
        model = "gpt-4o",
        messages = [
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Example usage
user_question = "tell me about ibm"
response = get_openai_response(user_question)
print("the response is:",response)