from flask import Blueprint
from flask_apispec import FlaskApiSpec
from flask_restful import Api

from resources.task import Task

api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint)

# API routes -- start
api.add_resource(Task, "/task")
# API routes -- end


docs = FlaskApiSpec()

# API docs -- start
docs.register(Task, blueprint="api")
# API docs -- end
