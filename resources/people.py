from flask_apispec import marshal_with, use_kwargs
from utils import Resource
from resources.talk import allow_only_talk_conference

# Abstract People -- Start
class Person(Resource):
    person_type=None

    @allow_only_talk_conference
    @marshal_with(None, code=201, apply=False)
    def delete(self):
        if not self.person_type:
            raise NotImplementedError("person_type not set")
        # remove a person
        "", 201

 
class People(Resource):
    person_type=None

    @allow_only_talk_conference
    @marshal_with(None, code=201, apply=False)
    def post(self):
        if not self.person_type:
            raise NotImplementedError("person_type not set")
        # add a person
        "", 201

# Abstract People -- END


class Speaker(Person):
    person_type = "speaker"

 
class Speakers(People):
    person_type = "speaker"

class Participant(Person):
    person_type = "participant"

 
class Participants(People):
    person_type = "participant"