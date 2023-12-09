from flask import Flask, render_template, request, Response

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('pages/index.html')


@app.route('/projet')
def projet():
    return render_template('pages/projet.html')


@app.route('/prompt', methods=['POST'])
def prompt():
    messages = request.json['messages']
    conversation = build_conversation_dict(messages=messages)
    return Response(event_stream(conversation), mimetype='text/event-stream')


def build_conversation_dict(messages: list) -> list[dict]:
    return [
        {"role": "user" if i % 2 == 0 else "assistant", "content": message}
        for i, message in enumerate(messages)
    ]


def event_stream(conversation: list[dict]):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        stream=True
    )
    for line in response:
        text = getattr(line.choices[0].delta, "content", "")
        if text:
            yield text


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)