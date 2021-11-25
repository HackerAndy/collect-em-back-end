from flask import Flask
from flask_restful import Api, Resource
from flasgger import Swagger


def create_app():
    app = Flask(__name__)
    prefix = '/api'

    # Create an APISpec
    template = {
      "swagger": "2.0",
      "basePath": "/api",
      "host": "127.0.0.1:5000",
      "info": {
        "title": "project",
        "description": "Project project developed by pickachu",
        "version": "1.0.0",
        "contact": {
          "name": "docdrew",
          "email": "docdrew@umich.edu",
        }
      }
    }

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

    api = Api(app)

    # a simple response that returns OK
    @app.route(prefix + '/')
    def send_ok():
        return 'OK'

    # a simple response controller that says hello
    class projectController(Resource):
        
        def get(self):
            """
            Get endpoint for greeting
            ---
            description:
                Retrieves Hello World greeting
            tags:
                - Greeting
            responses:
                - 200: Hello, World! greeting successfully retrieved
            """
            return 'Hello, World!'

    # Api resource routing
    api.add_resource(projectController, prefix + '/greeting')

    return app
