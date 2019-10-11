import json

import redis

broker = redis.Redis(host='localhost', port=6379, db=0)


def parse_event(event):
    channel = event['channel'].decode('utf-8')
    raw_data = event['data']
    if type(raw_data) != bytes:
        print('Invalid evet data type')
        data = None
    else:
        data = json.loads(raw_data.decode('utf-8'))
    return (channel, data)


def publish_event(event_name, data):
    broker.publish(event_name, json.dumps(data))
