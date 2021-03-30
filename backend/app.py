import json

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

todos = {
    0: {"id": "0", "name": "foo"}
}


class TodoSimple(Resource):
    def get(self, todo_id):
        response = jsonify(todos[todo_id])
        response.headers['Access-Control-Allow-Credentials'] = "true"
        return response
    
    def put(self, todo_id):
        todos[todo_id] = request.form["data"]
        return todos[todo_id]


api.add_resource(TodoSimple, '/api/<int:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
