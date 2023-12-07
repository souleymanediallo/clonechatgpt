from flask import Flask, render_template

import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('pages/index.html')


def build_conversation(messages: list) -> list[dict]:
    return [
        {"role": "user" if i % 2 == 0 else "assistant", "content": message}
        for i, message in enumerate(messages)
    ]


def event_stream(conversation: list[dict]):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        stream=True
    )
    for line in response:
        text = line.choices[0].delta.get("content", "")
        if text:
            yield text


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)