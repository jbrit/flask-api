from marshmallow import Schema, fields


class PersonSchema(Schema):
    id = fields.Int(dump_only=True)