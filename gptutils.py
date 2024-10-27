from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

systemPrompt = { "role": "system", "content": "You are here to teach kids about quantum physics" }
data = []

def get_response(incoming_msg):
    data.append({"role": "user", "content": incoming_msg})
    messages = [systemPrompt] + data
    response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages

            )
    content = response.choices[0].message.content
    return content
