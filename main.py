from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

class status(Resource):    
     def get(self):
         try:
            return {'data': 'Api running'}
         except: 
            return {'data': 'An Error Occurred during fetching Api'}

class Sum(Resource):
    def get(self, a, b):
        return jsonify({'data': a+b})


class Soma(Resource):
    def get(self):
        return {'soma':1+2}

api.add_resource(status,'/')
api.add_resource(Sum,'/add/<int:a>,<int:b>')
api.add_resource(Soma, '/soma/')

if __name__ == '__main__':
    app.run()