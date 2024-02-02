import os
from openai import OpenAI
import sys, signal
sys.path.append('..')
from functions.readenv    import read_envs_api_key
from functions.model_list import openai_models

# Set the current working directory to the directory of main.py
os.chdir(os.path.dirname(os.path.realpath(__file__)))
openai_api_key = read_envs_api_key()
client = OpenAI(api_key=openai_api_key)
openai_models(client)

if client.api_key is None:
    print("OpenAI API key not found. Make sure to set it in the .env file.")
else:
    # Define the prompt
    prompt = "What is the capital of Canada?"

    # Make a request to the OpenAI API
    response = client.completions.create(
        model="gpt-3.5-turbo",  # You can also use "text-davinci-002" or "text-davinci-001"
        prompt=prompt,
        max_tokens=50)

    # Get and print the generated text
    generated_text = response.choices[0].text
    print(f"Generated text: {generated_text}")
