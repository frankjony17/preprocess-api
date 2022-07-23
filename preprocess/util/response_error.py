
from flask import Blueprint, abort, jsonify

error_handler = Blueprint('error_handler', __name__)


error_dict = {
    400: {'detail': 'Bad Request, wrong syntax, '
                    'the request could not be understood by the server.'},
    401: {'detail': 'Bad Request, wrong base64, '
                    'Wrong base64 format, read Preprocess API documentation '
                    'in /docs for further questions.'},
    404: {'detail': 'Bad Request, required parameters missing, parameters '
                    'wasn\'t found.'},
    405: {'detail': 'Bad Request, required value false, the value of the '
                    'angle/scale parameter must be numeric (int).'},
}


def raise_error(code):
    if code > 200:
        abort(code)


def response(code):
    """Return response message according to request type of error.
    Args:
        code (int): Code of error.
    Returns:
        dict or None: Message and reason from request type of error.
    """
    return error_dict.get(code, None)


@error_handler.app_errorhandler(400)
def wrong_syntax(error):
    return jsonify(response(400)), 400


@error_handler.app_errorhandler(401)
def no_face(error):
    return jsonify(response(401)), 400


@error_handler.app_errorhandler(404)
def bad_image(error):
    return jsonify(response(404)), 400


@error_handler.app_errorhandler(405)
def bad_number(error):
    return jsonify(response(405)), 400
