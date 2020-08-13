# massages the flask reponse to send data as json and a status code

from flask import jsonify


def load_response(data, status_code):
    # jsonify returns a flask reponse object
    response = jsonify(data)
    response.status_code = status_code
    return response
