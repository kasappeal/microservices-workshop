import redis

broker = redis.Redis(host='localhost', port=6379, db=0)
