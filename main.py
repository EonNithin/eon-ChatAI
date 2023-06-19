# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

'''
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''

import time

import openai
import os
'''
OpenAI Authentication
Sign up at: https://platform.openai.com/signup
Generate a new API Key
'''
os.environ['OPENAI_API_KEY'] = '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'
openai.api_key = os.getenv('OPENAI_API_KEY')

'''
Load the key from a file
'''
'''
with open('key.txt', 'r') as f:
    api_key = f.read().strip('\n')
    assert api_key.startswith('sk-'), 'Error loading the API key. The API key starts with "sk-"'
openai.api_key = api_key
'''

'''inputs to Eon Ai
Looping chat'''
questions = list()
bot_responses = list()
messages = list()

system_prompt = input('System prompt:')
if system_prompt == '':
    system_prompt = 'Answer as concisely as possible. '

messages.append({"role": "system", "content": system_prompt})

while True:
    current_question = input('Me:')

    if current_question.lower() in ['exit', 'quit']:
        print('Chat Bot: I was happy to asssist you. Bye bye!')
        time.sleep(2)
        break

    if current_question.lower() == '':
        continue

    messages.append({"role": "user", "content": current_question})
    questions.append(current_question)

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7
        #max_tokens = 3000
    )

    current_response = completion.choices[0].message.content
    print(f'\nChat Bot: {current_response}')
    bot_responses.append(current_response)

    messages.append({"role": "assistant", "content": current_response})

    print('\n' + '-' * 50 + '\n')

