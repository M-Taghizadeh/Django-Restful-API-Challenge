from dynamorm import DynaModel
from marshmallow import fields


class Devices(DynaModel):
    class Table:
        name = "Test_DevicesDB"
        hash_key = "id"
        read = 25
        write = 5

    class Schema:
        id = fields.String()
        deviceModel = fields.String()
        name = fields.String()
        note = fields.String()
        serial = fields.String()