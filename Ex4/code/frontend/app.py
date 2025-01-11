from flask import Flask, request, make_response, jsonify
import requests
from requests.exceptions import ConnectionError, HTTPError
from datetime import date
import random

def create_header(X,response):
    value = random.randint(0,X)
    response.headers['exam'] = str(value)
    return value, response

BACKEND_URL = 'http://backend:8000'

def calc(X):
    try:
        URL = BACKEND_URL + f'/mod?a={X}&b={7}'
        x = requests.get(URL, timeout=1)
        x.raise_for_status()
        res = x.json()
        return int(res['s'])
    except ConnectionError:
        return make_response('Backend service is down\n', 400)
    except HTTPError:
        return make_response('Invalid input\n', 400)

app = Flask(__name__, instance_relative_config=True)

def create_value(X, r):
    a = create_header(X,r)[1].headers
    b = calc(X)
    a.set('exam', str(b)+"a")
    return a

@app.route('/<op>', methods=['GET'])
def operation(op):
    if op not in ['add', 'sub']:
        return make_response('Invalid operation\n', 404)
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    try:
        URL = BACKEND_URL + f'/{op}?a={a}&b={b}'
        x = requests.get(URL, timeout=1)
        x.raise_for_status()
        res = x.json()
    except ConnectionError:
        return make_response('Backend service is down\n', 400)
    except HTTPError:
        return make_response('Invalid input\n', 400)
    return res


def create_app():
    return app

def create_secret(X,response):
    example = date.today()
    ran, value = create_header(X,response)
    b = create_value(X,response)
    b['exam'] = "b"+b['exam']
    response.headers['exan'] = example.strftime("%Y")+example.strftime("%m")+example.strftime("%d")
    response.set_cookie('exam', str(4*(ran+6)/2-ran*2)+"a")
    return response



@app.route('/secret', methods=['GET'])
def get_secret():
    X = request.args.get('X', type = int)
    response = make_response(jsonify(exam=X), 200)
    return create_secret(X,response)
