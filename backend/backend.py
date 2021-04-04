from flask import Flask, request

from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from models import diffie_hellman
from models import rsa

app = Flask(__name__)
api = Api(app)

CORS(app)


@app.route("/")
def hello():
    return jsonify({'text': 'Hello World!'})


api.add_resource(diffie_hellman.Diffie_Hellman, '/getPublicKeys',
                 '/userInfo/<key>/<publicKey1>/<privateKey1>/<publicKey2>/<privateKey2>', '/getKeyGenerated/<key>', '/getSecretKeyGenerated/<key>')
api.add_resource(rsa.RSA, '/encryptDecryptData/<data>')


if __name__ == '__main__':
    app.run(port=5002)
