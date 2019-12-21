from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "William"
        "age": 27,
        "occupation": "IT Technician"
    }
    
]


           