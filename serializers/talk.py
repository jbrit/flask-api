from marshmallow import Schema, fields

from serializers.people import PersonSchema

class TalkSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    duration = fields.Int(required=True) # in minutes
    date_time = fields.DateTime(required=True)
    description = fields.Str(required=True)
    speakers = fields.Method('get_speakers')
    participants = fields.Method('get_participants')

    def get_speakers(self, talk):
        speakers = list(map(PersonSchema().dump, list(filter(lambda person: str(person.person_type) == "speaker", talk.people))))
        return speakers
    
    def get_participants(self, talk):
        participants = list(map(PersonSchema().dump, list(filter(lambda person: str(person.person_type) == "participant", talk.people))))
        return participants