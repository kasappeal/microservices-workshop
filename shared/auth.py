from flask_jwt import JWT, _default_jwt_payload_handler


def identity(payload):
    return payload['identity']


def make_payload(identity):
    result = _default_jwt_payload_handler(identity)
    result['identity'] = {'id': identity.id, 'username': identity.username}
    return result


jwt = JWT(identity_handler=identity)
jwt.jwt_payload_handler(callback=make_payload)
