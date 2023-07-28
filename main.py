import openai
import time
import pandas as pd
import os

# Load the API key from a file
with open('key.txt', 'r') as f:
    api_key = f.read().strip('\n')
    assert api_key.startswith('sk-'), 'Error loading the API key. The API key starts with "sk-"'

def parse_excel(file_path):
    df = pd.read_excel(file_path)  # Assuming your Excel file has header rows
    return df

openai.api_key = api_key

# Inputs to ChatGPT
questions = list()
bot_responses = list()
messages = list()

system_prompt = input('System prompt:')
if system_prompt == '':
    system_prompt = 'Answer as concisely as possible.'

messages.append({"role": "system", "content": system_prompt})

while True:
    current_question = input('Me:')

    if current_question.lower() in ['exit', 'quit']:
        print('Chat Bot: I was happy to assist you. Goodbye!')
        time.sleep(2)
        break

    if current_question.lower() == '':
        continue

    messages.append({"role": "user", "content": current_question})
    questions.append(current_question)

    # Generate completion response with ChatGPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": current_question}
        ],
        temperature=0.5,
        max_tokens=500,
        top_p=0,
        frequency_penalty=0,
        presence_penalty=0
    )

    current_response = response['choices'][0]['message']['content'].strip()
    print(f'\nChat Bot: {current_response}')
    bot_responses.append(current_response)

    messages.append({"role": "assistant", "content": current_response})

    print('\n' + '-' * 50 + '\n')
