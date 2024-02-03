from openai import OpenAI

def openai_models(client):
    model_list = client.models.list()
    
    # Printing out a list of all aviable models.
    print(f'List of OpenAI models:{model_list}\n')
    # Iterate over the list of models and print their details
    for model in model_list:
        print(f"Model ID: {model.id}")
        print(f"Created: {model.created}")
        print(f"Object: {model.object}")
        print(f"Owned By: {model.owned_by}")
        print("------------------------")
    
    return 