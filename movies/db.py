from pymongo import MongoClient

DB_NAME = 'movies'

connection = MongoClient(f'mongodb://localhost:27017/{DB_NAME}')
db_client = connection[DB_NAME]
