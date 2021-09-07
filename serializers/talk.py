from marshmallow import Schema, fields


class TalkSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    # duration as fraction of hours
    duration = fields.Float()
    start_date_time = fields.DateTime()
    description = fields.Str()
    # TODO: update user schema
    participants = fields.Nested('UserSchema', many=True)
    speakers = fields.Nested('UserSchema', many=True)
