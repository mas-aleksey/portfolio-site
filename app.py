import os
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from requests import post, RequestException


TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'


app = Flask(__name__)
Bootstrap(app)


@app.route('/', methods=['GET'])
def index():
    notification(str(request.headers))
    return render_template('index.html')


def notification(message: str) -> None:
    try:
        response = post(URL, data={'chat_id': CHAT_ID, 'text': message})
    except RequestException as exc:
        print(f'Send message error: {exc}')
    else:
        print(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0')


