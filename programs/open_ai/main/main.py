import os
import openai

# API KEY DELETE THIS LATER OH MY GOD SCARY
# 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
# Set your OpenAI API key
openai.api_key = 'your-api-key'  # Replace with your actual API key

# Get the OpenAI API key from the environment variable
openai.api_key = os.environ.get('OPENAI_API_KEY')

# Define the prompt
prompt = "What is the capital of Canada?"

# Make a request to the OpenAI API
response = openai.Completion.create(
    engine="text-davinci-003",  # You can also use "text-davinci-002" or "text-davinci-001"
    prompt=prompt,
    max_tokens=50
)

# Get and print the generated text
generated_text = response['choices'][0]['text']
print(f"Generated text: {generated_text}")
