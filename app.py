
import os
import gradio as gr
import openai

os.environ['OPENAI_API_KEY'] = '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'
openai.api_key = os.getenv('OPENAI_API_KEY')

questions = list()
bot_responses = list()
messages = list()

system_prompt = input('System prompt:')
if system_prompt == '':
    system_prompt = 'Answer as concisely as possible. '

messages.append({"role": "system", "content": system_prompt})

def respond(message, chat_history):
    if isinstance(message, str):
        current_question = message
    else:
        current_question = message["content"]

    #current_question = message["content"]

    if current_question.lower() in ['exit', 'quit']:
        return 'Chat Bot: I was happy to assist you. Bye bye!', chat_history

    if current_question.lower() == '':
        return '', chat_history

    messages.append({"role": "user", "content": current_question})
    questions.append(current_question)

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7
        # max_tokens = 3000
    )

    current_response = completion.choices[0].message.content
    bot_responses.append(current_response)

    messages.append({"role": "assistant", "content": current_response})

    return 'Chat Bot:' + current_response

demo = gr.Interface(fn=respond, inputs="textbox", outputs="textbox", title="Chatbot Demo")

if __name__ == "__main__":
    demo.launch()
