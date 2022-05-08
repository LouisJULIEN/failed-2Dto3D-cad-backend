from cerberus import Validator
from flask import Flask, request

from main import two_D_to_three_D

app = Flask(__name__)


# FLASK_ENV=development FLASK_APP=web flask run

@app.route("/health-check", methods=['GET'])
def health_check():
    return {'msg': 'ok'}


@app.route("/version")
def get_version():
    return {'version': 1.0}


raw_a_shape_projection_schema = {
    'type': 'dict',
    'require_all': True,
    'schema': {
        'type': {
            'type': 'string',
            'allowed': ['polygon'],
        },
        'vertices': {
            'type': 'dict',
            'keysrules': {'type': 'integer'},
            'allow_unknown': True,
        },
        'edges': {
            'type': 'dict',
            'keysrules': {'type': 'integer'},
            'allow_unknown': True,
        },
    }
}

raw_projection_schema = {
    'type': 'dict',
    'keysrules': {'type': 'string', 'regex': '[a-z0-9-]+'},
    'valuesrules': raw_a_shape_projection_schema,
}

raw_two_D_schema = {
    'xy': raw_projection_schema,
    'xz': raw_projection_schema,
    'yz': raw_projection_schema,
}

validator_reconstruct = Validator(raw_two_D_schema)


@app.route("/reconstruct", methods=['POST'])
def reconstruct():
    parsed_payload = request.get_json()
    if not validator_reconstruct.validate(parsed_payload):
        return validator_reconstruct.errors, 400

    return two_D_to_three_D(parsed_payload)
