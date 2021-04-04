from flask import request, render_template, make_response, Flask, jsonify, current_app as app
from flask_restful import Api, Resource
import sys


class RSA(Resource):
    def get(self, data=None):
        p = 53
        q = 59
        n = p*q
        e = 3
        k = 2
        coef = int((p-1)*(q-1))
        n*pi(1-1/p)
        n*pi(1-1/q)
        d = int((k * coef + 1)/e)

        if data != None:
            encrypt = []
            decrypt = []
            dataarr = data.split(",")
            for i in dataarr:
                print(int(i))
                encrypt.append(pow(int(i), e) % n)
                decrypt.append(pow(int(i), d) % n)

            return {"D": decrypt, "E": encrypt}
