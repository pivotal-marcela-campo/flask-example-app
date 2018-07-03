import json
from flask import Flask, current_app, request

flasktestapp = Flask(__name__)


@flasktestapp.route('/')
def todo_list():
    db = current_app.config['DATABASE']
    return json.dumps(db.all())

@flasktestapp.route('/', methods=['POST'])
def add_todo():
    db = current_app.config['DATABASE']
    db.add_todo(request.json)
    return '', 201


@flasktestapp.route('/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    db = current_app.config['DATABASE']
    db.update_todo(todo_id, request.json)
    return '', 200
