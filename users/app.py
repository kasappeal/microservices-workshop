from flask import Flask, jsonify
from flask_jwt import jwt_required, current_identity

from shared.auth import jwt
from users.db import db_client


class User(object):
    def __init__(self, id, username):
        self.id = id
        self.username = username


def authenticate(username, password):
    result = db_client.users.find_one({'username': username, 'password': password})
    return User(str(result['_id']), result['username'])


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Bruce Wayne is Batman'

jwt.authentication_callback = authenticate
jwt.init_app(app)


@app.route('/me')
@jwt_required()
def me():
    return jsonify({'id': current_identity['id'], 'username': current_identity['username']})
