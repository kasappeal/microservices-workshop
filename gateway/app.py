import requests
from flask import Flask, request, jsonify
from flask_jwt import jwt_required, current_identity

from shared.auth import jwt


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Bruce Wayne is Batman'
jwt.init_app(app)

MOVIES_SERVICE_URL = 'http://127.0.0.1:5001'
REVIEWS_SERVICE_URL = 'http://127.0.0.1:5002'


@app.route('/movies/')
def movies_list():
    url = f'{MOVIES_SERVICE_URL}/movies/'
    response = requests.get(url)
    body = response.json()
    return jsonify(body), response.status_code


@app.route('/movies/<string:movie_id>')
def movie_detail(movie_id):
    url = f'{MOVIES_SERVICE_URL}/movies/{movie_id}'
    response = requests.get(url)
    movie = response.json()
    url = f'{REVIEWS_SERVICE_URL}/reviews/{movie_id}'
    response = requests.get(url)
    reviews = response.json()
    movie['reviews_list'] = reviews
    return jsonify(movie)


@app.route('/reviews/<string:movie_id>', methods=['POST'])
@jwt_required()
def movie_review(movie_id):
    url = f'{REVIEWS_SERVICE_URL}/reviews/{movie_id}'
    response = requests.post(url, data=request.json)
    result = response.json()
    return jsonify(result), response.status_code
