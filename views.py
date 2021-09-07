from flask import Blueprint
from flask_apispec import FlaskApiSpec
from flask_restful import Api

from resources.talk import Talk

api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint)

# API routes -- start
api.add_resource(Talk, "/talk")
# API routes -- end


docs = FlaskApiSpec()

# API docs -- start
docs.register(Talk, blueprint="api")
# API docs -- end
