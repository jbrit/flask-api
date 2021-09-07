from flask import Flask
from flask_restful import abort
from webargs.flaskparser import parser
from config import app_config
from views import api_blueprint, docs


# This error handler is necessary for usage with Flask-RESTful
# pylint: disable=unused-argument
@parser.error_handler
def handle_request_parsing_error(err, req, schema, **kwargs):
    """webargs error handler that uses Flask-RESTful's abort function to return
    a JSON error response to the client.
    """
    abort(422, errors=err.messages)


def create_app():
    app = Flask(__name__)
    app.config.update(app_config)
    app.register_blueprint(api_blueprint)
    docs.init_app(app)
    return app
