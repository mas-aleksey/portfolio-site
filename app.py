import os
from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from requests import post, RequestException
from context import CONTEXT, Language


TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'


app = Flask(__name__)
Bootstrap(app)


@app.route('/', methods=['GET'])
def index():
    if 'ru' in request.headers.get('Accept-Language'):
        return redirect('ru')
    return redirect('en')


@app.route('/ru', methods=['GET'])
def ru():
    return main_page(Language.RUS)


@app.route('/en', methods=['GET'])
def en():
    return main_page(Language.ENG)


def main_page(local: Language):
    notification(str(request.headers))
    return render_template('index.html', context=CONTEXT[local])


def notification(message: str) -> None:
    try:
        response = post(URL, data={'chat_id': CHAT_ID, 'text': message})
    except RequestException as exc:
        print(f'Send message error: {exc}')
    else:
        print(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0')


