from functools import wraps
from flask_restful import abort
from flask_apispec import marshal_with, use_kwargs
from utils import Resource
import models


def allow_only_talk_conference(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        talk_id = kwargs.get("talk_id")
        conference_id = kwargs.get("conference_id")
        talk = models.Talk.query.get_or_404(talk_id)
        if talk.conference_id == conference_id:
            abort(403, message="You don't have permission to view this.")
        return func(*args, **kwargs)
    return wrapper
    
class Talk(Resource):
    @allow_only_talk_conference
    @marshal_with(None, code=201, apply=False)
    def put(self):
        # edit a talk
        "", 201

 
class Talks(Resource):
    @marshal_with(None, apply=False)
    def get(self):
        # List talks in a conference
        "", 200

    @marshal_with(None, code=201, apply=False)
    def post(self):
        # add a talk
        "", 201