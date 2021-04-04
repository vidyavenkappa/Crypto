from flask import request, render_template, make_response, Flask, jsonify, current_app as app
from flask_restful import Api, Resource
import sys


class Diffie_Hellman(Resource):

    def get(self, key=None, publicKey1=None, publicKey2=None, privateKey1=None, privateKey2=None):

        if publicKey1 != None and publicKey2 != None and privateKey1 != None and privateKey2 != None and key == "info":
            with open("test.txt", "w") as fo:
                fo.write(publicKey1 + " "+privateKey1+"\n")
                fo.write(publicKey2 + " "+privateKey2)
            return make_response(jsonify(success='true', message="successful!!"), 200)

        elif publicKey1 == None and publicKey2 == None and privateKey1 == None and privateKey2 == None and key == None:
            with open("test.txt") as fp:
                line = fp.readline()
                wordArr = line.split(" ")
                pubKey1 = wordArr[0]
                line = fp.readline()
                wordArr = line.split(" ")
                pubKey2 = wordArr[0]
            return {"User1": pubKey1, "User2": pubKey2}

        elif publicKey1 == None and publicKey2 == None and privateKey1 == None and privateKey2 == None and key == "key":
            with open("test.txt") as fp,  open("key.txt", "w") as fo:
                line = fp.readline()
                wordArr = line.split(" ")
                pubKey1 = int(wordArr[0])
                privKey1 = int(wordArr[1])
                line = fp.readline()
                wordArr = line.split(" ")
                pubKey2 = int(wordArr[0])
                privKey2 = int(wordArr[1])

                key1 = int(pow(pubKey2, privKey1) % pubKey1)
                key2 = int(pow(pubKey2, privKey2) % pubKey1)

                fo.write(str(key1)+"\n")
                fo.write(str(key2))

            return {"User1": key1, "User2": key2}

        elif publicKey1 == None and publicKey2 == None and privateKey1 == None and privateKey2 == None and key == "secret":
            with open("key.txt") as fo, open("test.txt") as fp:
                key1 = int(fo.readline())
                key2 = int(fo.readline())
                line = fp.readline()
                print(line, file=sys.stdout)
                wordArr = line.split(" ")
                pubKey1 = int(wordArr[0])
                privKey1 = int(wordArr[1])
                line = fp.readline()
                print(line, file=sys.stdout)
                wordArr = line.split(" ")
                pubKey2 = int(wordArr[0])
                privKey2 = int(wordArr[1])

                secretkey1 = int(pow(int(key2), privKey1) % pubKey1)
                print(line, file=sys.stdout)
                secretkey2 = int(pow(int(key1), privKey2) % pubKey1)

            return {"User1": secretkey1, "User2": secretkey2}

        return 0
