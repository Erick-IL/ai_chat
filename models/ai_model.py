from database.database_info import create_user, get_user_history
from dotenv import load_dotenv
from datetime import datetime
from openai import OpenAI
import json
import os

training_data = 'Seu nome é roberto, responda com respostas curtas'

def model_request(training_data, user_message, history_chat='') -> str:

    load_dotenv()
    system_message = f"{training_data} + {history_chat}"
    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv('OPEN_ROUTE_KEY'),
    )
    completion = client.chat.completions.create(
    model="deepseek/deepseek-chat-v3:free",
    messages=[
        {"role": "system",
         "content": system_message
         },
        {
        "role": "user",
        "content": user_message,
        }
    ])
    
    return completion.choices[0].message.content 

def send_message(user_id, message):
    if os.path.exists("functions/message.json") and os.path.getsize("functions/message.json") > 0:
        with open("functions/message.json", "r") as file: 
            data = json.load(file)
    else:
        data = {"messages": []}

    data['messages'].append({"id": user_id, "message": message})

    with open("functions/message.json", "w") as file:
        json.dump(data, file, indent=2)

def generate_and_send_responses():
    with open("functions/info.json", "r") as file:
        try:
            info = json.load(file)
        except Exception:
            return
        
        try:
            for user in info['users']:
                print('informações carregadas')
                user_id, user_history = get_user_history(user)
                user_message = info['users'].get(user_id, [])

                for message in user_message:
                    print('Gerando resposta')
                    request = model_request(training_data, message, user_history)
                    send_message(user_id, request)
                    create_user(user_id, [{"role": "user", "text": f'{user_message}, Timestamp: {datetime.now()}'}, {"role": "system", "text": f'{request}, Timestamp: {datetime.now()}'}])
                    
                    del info['users']
                    with open("functions/info.json", "w") as file:
                        print("Json limpo")
                        json.dump(info, file, indent=2)
        except Exception:
            return



