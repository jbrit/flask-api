from flask_restful import abort
from flask_sqlalchemy import model
from serializers.people import PersonSchema
from flask_apispec import marshal_with, use_kwargs
from utils import Resource
from resources.talk import allow_only_talk_conference, allow_only_created_conference
import models
from functools import wraps


def allow_only_created_talk(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        models.Talk.query.get_or_404(kwargs.get("talk_id"))
        return func(*args, **kwargs)
    return wrapper



# Abstract People -- Start
class Person(Resource):
    person_type=None

    @allow_only_created_conference
    @allow_only_created_talk
    @allow_only_talk_conference
    @marshal_with(None, code=204, apply=False)
    def delete(self, conference_id, person_id, talk_id):
        if not self.person_type:
            raise NotImplementedError("person_type not set")
        person = models.Person.query.get_or_404(person_id)
        if person.talk_id != talk_id:
            abort(400, message="{} not in talk".format(self.person_type))
        if self.person_type != str(person.person_type):
            abort(400, message="User cannot be deleted as a {} in this talk".format(self.person_type))
        models.db.session.delete(person)
        models.db.session.commit()
        return "", 204

 
class People(Resource):
    person_type=None

    @allow_only_created_conference
    @allow_only_created_talk
    @allow_only_talk_conference
    @use_kwargs(PersonSchema())
    @marshal_with(PersonSchema(), code=201)
    def post(self, conference_id, talk_id, **kwargs):
        if not self.person_type:
            raise NotImplementedError("person_type not set")
        talk = models.Talk.query.get_or_404(talk_id)
        if not self.person_type == "speaker" and not self.person_type == "participant":
            abort(400, message="person_type must be speaker or participant")
        person = models.Person(**kwargs, talk_id=talk_id, person_type=self.person_type)
        models.db.session.add(person)
        models.db.session.commit()
        return person, 201

# Abstract People -- END


class Speaker(Person):
    person_type = "speaker"

 
class Speakers(People):
    person_type = "speaker"

class Participant(Person):
    person_type = "participant"

 
class Participants(People):
    person_type = "participant"