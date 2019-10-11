from flask import Flask, request, jsonify
from flask_jwt import jwt_required, current_identity

from shared.auth import jwt


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Bruce Wayne is Batman'

jwt.init_app(app)

