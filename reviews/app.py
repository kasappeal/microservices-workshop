import requests
from bson import ObjectId
from flask import Flask, request, jsonify
from flask_jwt import jwt_required, current_identity

from shared.auth import jwt
from shared.broker import publish_event
from .db import db_client

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Bruce Wayne is Batman'
jwt.init_app(app)


@app.route('/reviews/<string:movie_id>', methods=['POST'])
@jwt_required()
def movie_review(movie_id):
    data = request.json
    url = f'http://localhost:5001/movies/{movie_id}'
    response = requests.get(url)
    if not response.ok:
        return jsonify({'error': 'Movie not found'}), 404
    review = {
        'user': current_identity['id'],
        'movie': movie_id,
        'comments': data['comments'],
        'rating': data['rating']
    }
    db_client.reviews.insert(review)
    del review['_id']
    publish_event('new_review', review)
    return jsonify({'result': 'success'}), 201


@app.route('/reviews/<string:movie_id>', methods=['GET'])
def movie_reviews(movie_id):
    results = db_client.reviews.find({'movie': movie_id})
    reviews = []
    for result in results:
        reviews.append({
            'id': str(result['_id']),
            'user': result['user'],
            'movie': result['movie'],
            'comments': result['comments'],
            'rating': result['rating']
        })
    return jsonify(reviews)
