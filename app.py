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


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)