from shared.broker import broker, parse_event

pubsub = broker.pubsub()

events = ['*']
pubsub.psubscribe(events)

print('Listening...')
for event in pubsub.listen():
    channel, data = parse_event(event)
    print(f'Received {channel}: {data}')
    # TODO PROCESS HERE YOUR EVENTS
    print('Listening...')
