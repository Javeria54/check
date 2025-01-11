from flask import Flask, request, make_response, jsonify
from datetime import datetime
import random
import operator
from functools import reduce


app = Flask(__name__, instance_relative_config=True)

def get_input_and_compute(op, name):
    a = request.args.get('a', 0, type=float)
    b = request.args.get('b', 0, type=float)
    lst = request.args.get('lst', type=str)
    if lst is not None:
        lst = eval(lst) # get list from string
        if (op in [operator.truediv, operator.mod]) and any(x == 0 for x in lst[1:]):
            return make_response('Cannot divide by zero\n', 400)
        value = reduce(op, lst)
        return value
    return op(a,b)

@app.route('/add')
def add():
    value = get_input_and_compute(operator.add, "+")
    return make_response(jsonify(s=value), 200)
    
@app.route('/sub')
def sub():
    value = get_input_and_compute(operator.sub, "-")
    return make_response(jsonify(s=value), 200)

@app.route('/mul')
def mul():
    value = get_input_and_compute(operator.mul, "*")
    return make_response(jsonify(s=value), 200)

@app.route('/div')
def div():
    value = get_input_and_compute(operator.truediv, "/")
    return make_response(jsonify(s=value), 200)

@app.route('/mod')
def mod():
    value = get_input_and_compute(operator.mod, "%")
    return make_response(jsonify(s=value), 200)

@app.route('/random')
def secure_random():
    a = request.args.get('a', 0, type=float)
    b = request.args.get('b', 0, type=float)
    a = int(a)
    b = int(b)
    value = random.randint(a,b)
    return make_response(jsonify(s=value), 200)

def create_app():
    return app

def addLog():
    payload = request.json
    db = None
    key = payload["time"]
    value = payload["log"]
    with app.app_context():
        log = db.session.execute('SELECT * FROM log WHERE log = \'%s\' AND time = \'%s\''% (value, key)).first()
        if log is None:
            db.session.add(key, value)
            db.session.commit()
        else:
            # print also log
            return make_response(jsonify(error="log already exists", log=log), 400)
    return make_response(jsonify('ok'),200)
