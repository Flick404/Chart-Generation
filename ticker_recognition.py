from openai import OpenAI
import os
from dotenv import load_dotenv

def get_ticker_symbol(user_input):
    # Load environment variables from .env file
    load_dotenv()

    # Get API key from environment variable
    api_key = os.getenv("OPENAI_API_KEY")

    # Ensure API key is available
    if not api_key:
        raise ValueError("OpenAI API key not found in environment variables")

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": f"Can you provide me with the Yahoo Finance ticker symbol for '{user_input}'? Please respond only with the ticker symbol."}
        ],
        temperature=0.1,
        max_tokens=28,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extracting the ticker symbol from the response
    ticker = response.choices[0].message.content.strip()
    return ticker
