from rest_framework import serializers
from rest_framework.serializers import Serializer


class DeviceSerializer(Serializer):
    id = serializers.CharField(max_length=50, allow_null=False)
    deviceModel = serializers.CharField(max_length=50, allow_null=False)
    name = serializers.CharField(max_length=100, allow_null=False)
    note = serializers.CharField(max_length=1000, allow_null=False)
    serial = serializers.CharField(max_length=50, allow_null=False)

    def validate_id(self, value):
        id = value.replace("/devices/id", "")

        if not id.isdigit():
            raise serializers.ValidationError(
                "id field must be in this format: /devices/id1"
            )

        return value

    def validate_deviceModel(self, value):
        device_model = value.replace("/devicemodels/id", "")

        if not device_model.isdigit():
            raise serializers.ValidationError(
                "deviceModel field must be in this format /devicemodels/id1"
            )

        return value
