import marshmallow
from marshmallow import fields


class PlayerSchema(marshmallow.Schema):
    id = fields.Integer(dump_only=True)
    Name = fields.String()
    Stage = fields.Integer()
    Action = fields.Integer()