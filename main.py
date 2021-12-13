import os
import sys

from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def calculator_home_page_str():
    return "Welcome to the greatest calculator ever !"


@app.route('/add')
def add():
    first = int(request.args.get("first"))
    second = int(request.args.get("second"))
    res = first + second
    return f'{first} + {second} = {res}'


if __name__ == '__main__':
    print(sys.version)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT')))