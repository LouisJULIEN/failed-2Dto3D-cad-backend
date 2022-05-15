
from cerberus import Validator
from flask import Flask, request
from flask_cors import CORS

from main import two_D_to_three_D
from utils import env_is_local

app = Flask(__name__)

if env_is_local():
    print("Authorising CORS for local env")
    cors = CORS(app)


@app.route("/health-check", methods=['GET'])
def health_check():
    return {'msg': 'ok'}


@app.route("/version", methods=['GET'])
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
            'keysrules': {'type': 'string'},
            'allow_unknown': True,
        },
        'edges': {
            'type': 'dict',
            'keysrules': {'type': 'string'},
            'allow_unknown': True,
        },
    }
}

raw_two_D_schema = {
    'xy': raw_a_shape_projection_schema,
    'xz': raw_a_shape_projection_schema,
    'yz': raw_a_shape_projection_schema,
}

validator_reconstruct = Validator(raw_two_D_schema)


@app.route("/reconstruct", methods=['POST'])
def reconstruct():
    parsed_payload = request.get_json()
    if not validator_reconstruct.validate(parsed_payload):
        return validator_reconstruct.errors, 400

    return two_D_to_three_D(parsed_payload)


if __name__ == '__main__' and env_is_local():
    app.run(debug=True, port=8000)
