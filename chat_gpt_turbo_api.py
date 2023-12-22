from openai import OpenAI
from IPython.display import display

def chat_gpt(prompt):
    api_key = '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'
    client = OpenAI(api_key=api_key)
    chat_completion = client.chat.completions.create(
        messages = [
            {
            "role" : "user",
            "content" : prompt},
        ],
        model = "gpt-3.5-turbo")
    text_to_speak = (chat_completion.choices[0].message.content)
    print(text_to_speak)
