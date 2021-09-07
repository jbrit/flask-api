from marshmallow import Schema, fields


class ConferenceSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    start_date = fields.DateTime(required=True)
    end_date = fields.DateTime(required=True)