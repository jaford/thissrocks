import os

def read_envs_api_key():
    
    # THIS IS NOT WORKING HOW I THINK IT DOES AND I AM LOOSING MY SHIT
    # Get the absolute path to the .env file
    # print("Current working directory:", os.getcwd())
    # env_file_path = os.path.abspath('/Users/hunterpimparatana/Documents/practice_code/source/thissrocks/programs/open_ai/functions/.env')
    
    env_file_path = os.path.abspath('.env')
    print(env_file_path)

    # Load environment variables from .env file
    with open(env_file_path) as f:
        lines = f.readlines()
        for line in lines:
            key, value = line.strip().split("=")
            os.environ[key] = value
            
    # Get the OpenAI API key from the environment variable
    openai_api_key = os.environ.get('OPENAI_API_KEY')
    
    return openai_api_key