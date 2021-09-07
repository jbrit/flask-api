from flask_apispec import marshal_with, use_kwargs
from utils import Resource

class Talk(Resource):
    @marshal_with(None, apply=False)
    def get(self):
        "", 200
    @marshal_with(None, code=201, apply=False)
    def post(self):
        "", 201