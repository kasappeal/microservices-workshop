from flask import Flask, request, jsonify
from flask_jwt import jwt_required, current_identity

from shared.auth import jwt
from .db import db_client

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Bruce Wayne is Batman'
jwt.init_app(app)
