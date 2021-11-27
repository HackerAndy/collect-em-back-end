import os
from flask import Flask
from flask_cors import CORS
from flask.json import JSONEncoder
from datetime import datetime
from bson import json_util, ObjectId
from flasgger import Swagger

from app.collectibles.collectibles_api import collectibles_api_v1

class MongoJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, ObjectId):
            return str(obj)
        return json_util.default(obj, json_util.CANONICAL_JSON_OPTIONS)
def create_app():

    app = Flask(__name__)
        # Create an APISpec

    template = {
      "swagger": "2.0",
      "basePath": "/api",
      "host": "127.0.0.1:5000",
      "info": {
        "title": "Gotta collect ‘em all",
        "description": "Project developed by Pickachu",
        "version": "1.0.0",
        "contact": {
          "name": "docdrew",
          "email": "docdrew@umich.edu",
        }
      }
    }

    CORS(app)
    app.config['SWAGGER'] = {
        'title': 'project',
        'uiversion': 3,
        "specs": [
            {
                "endpoint": 'api-docs',
                "route": '/api-docs'
            }
        ],
        "specs_route": "/swagger-ui/"
    }
    swagger = Swagger(app, template=template)

    app.json_encoder = MongoJsonEncoder
    app.register_blueprint(collectibles_api_v1)

    return app

