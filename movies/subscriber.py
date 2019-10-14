from bson import ObjectId

from movies.db import db_client
from shared.broker import broker, parse_event

pubsub = broker.pubsub()

events = ['new_review']
pubsub.psubscribe(events)

print('Listening...')
for event in pubsub.listen():
    channel, data = parse_event(event)
    print(f'Received {channel}: {data}')
    if channel == 'new_review' and data is not None:
        movie_id = data['movie']
        rating = data['rating']
        movie = db_client.movies.find_one({'_id': ObjectId(movie_id)})
        movie['reviews'] += 1
        new_rating = movie['rating'] + rating
        db_client.movies.update_one(
            {'_id': ObjectId(movie_id)},
            {'$set': {'rating': new_rating, 'reviews': movie['reviews']}})
    print('Listening...')
