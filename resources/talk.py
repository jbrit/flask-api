from functools import wraps
from serializers.talk import TalkSchema
from flask_restful import abort
from flask_apispec import marshal_with, use_kwargs
from utils import Resource, update_object_from_dict
import models


def allow_only_talk_conference(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        talk_id = kwargs.get("talk_id")
        conference_id = kwargs.get("conference_id")
        talk = models.Talk.query.get_or_404(talk_id)
        if talk.conference_id != conference_id:
            abort(403, message="You don't have permission to view this.")
        return func(*args, **kwargs)
    return wrapper

def allow_only_created_conference(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        models.Conference.query.get_or_404(kwargs.get("conference_id"))
        return func(*args, **kwargs)
    return wrapper
    
class Talk(Resource):
    @allow_only_talk_conference
    @allow_only_created_conference
    @use_kwargs(TalkSchema())
    @marshal_with(TalkSchema())
    def put(self, conference_id, talk_id, **kwargs):
        talk = models.Talk.query.get_or_404(talk_id)
        update_object_from_dict(talk, kwargs)
        return talk

 
class Talks(Resource):
    @allow_only_created_conference
    @marshal_with(TalkSchema(many=True))
    def get(self, conference_id):
        return models.Talk.query.filter_by(conference_id=conference_id).all()

    @allow_only_created_conference
    @use_kwargs(TalkSchema())
    @marshal_with(TalkSchema(), code=201)
    def post(self, conference_id, **kwargs):
        talk = models.Talk(**kwargs, conference_id=conference_id)
        models.db.session.add(talk)
        models.db.session.commit()
        return talk, 201