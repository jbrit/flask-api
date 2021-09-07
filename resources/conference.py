from serializers.conference import ConferenceSchema
from flask_apispec import marshal_with, use_kwargs
import models
from utils import Resource, update_object_from_dict

class Conference(Resource):
    @use_kwargs(ConferenceSchema(partial=True))
    @marshal_with(ConferenceSchema())
    def put(self, conference_id, **kwargs):
        conference = models.Conference.query.get_or_404(conference_id)
        update_object_from_dict(conference, kwargs)
        models.db.session.commit()
        return conference
        
    

class Conferences(Resource):
    @marshal_with(ConferenceSchema(many=True))
    def get(self):
        return models.Conference.query.all()

    @use_kwargs(ConferenceSchema())
    @marshal_with(ConferenceSchema(), code=201)
    def post(self, **kwargs):
        # Create a new conference
        conference = models.Conference(**kwargs)
        models.db.session.add(conference)
        models.db.session.commit()
        return conference, 201