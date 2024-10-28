from openai import OpenAI
from dotenv import load_dotenv
from flask import session
import tiktoken

load_dotenv()

client = OpenAI()
system_prompt = {"role": "system", "content": "You are a friendly tutor helping users with various topics."}

encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

def num_tokens_from_messages(messages):
    return sum(len(encoding.encode(msg["content"])) for msg in messages)


def get_response(user_msg):
    if 'chat_history' not in session:
        session['chat_history'] = []  # Create new chat history if not found

    session['chat_history'].append({"role": "user", "content": user_msg})

    messages = [system_prompt] + session['chat_history']

    while num_tokens_from_messages(messages) > 4000:
        session['chat_history'].pop(0)  # Remove oldest message

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    bot_content = response.choices[0].message.content
    session['chat_history'].append({"role": "assistant", "content": bot_content})

    return bot_content
