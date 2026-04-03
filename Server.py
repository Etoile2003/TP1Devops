from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "API TP1 Devops",
        "description": "Le swagger du tp1",
        "version": "1.0.0"
    },
    "host": "",  # This will be set dynamically
    "basePath": "/",
    "schemes": ["http"],
    "consumes": ["application/json"],
    "produces": ["application/json"]
}

swagger = Swagger(app, template=swagger_template, parse=True)

@app.before_request
def set_swagger_host():
    """Dynamically set the Swagger host."""
    swagger_template["host"] = request.host

@app.route("/", methods=["GET"], endpoint="hello_world")
def hello_world():
    """
    A simple hello world endpoint.
    ---
    tags:
      - Example
    responses:
      200:
        description: Returns a simple greeting message.
        schema:
          type: object
          properties:
            message:
              type: string
              example: Hello World!
    """
    return jsonify({"message": "Hello World!"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)