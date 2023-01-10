import os

import boto3
from dotenv import load_dotenv
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import DeviceSerializer

load_dotenv()


# Get the dynamodb using boto3
dynamodb = boto3.resource(
    "dynamodb",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION_NAME"),
)
table = dynamodb.Table("Device_DB")


class CreateDevice_API(APIView):
    """
    With this API we can create a new instance of the Device table
    """

    def post(self, request):
        serializer = DeviceSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data
            device = table.get_item(
                Key={
                    "id": data.get("id"),
                }
            )

            if "Item" in device:
                return Response(
                    status=status.HTTP_409_CONFLICT,
                    data={
                        "message": f'Item already exists with this id: {data.get("id")}.'
                    },
                )

            # Save Device
            table.put_item(Item=data)

            return Response(
                status=status.HTTP_201_CREATED,
                data={"message": "Item created successfully."},
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class GetDevice_API(APIView):
    """
    With this API, we can get all the information of an instance of the Device table with Device<pk>
    """

    def get(self, request, pk):
        device = table.get_item(
            Key={
                "id": f"/devices/id{pk}",
            }
        )

        # Check if device exists.
        if "Item" in device:
            serializer = DeviceSerializer(device["Item"])
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={"message": "This item does not exist."},
            )


class Get_All_Devices_API(APIView):
    "With this API, we can get all the information of all Devices in DeviceDB table"

    def get(self, request):
        devices = table.scan()

        if devices:
            return Response(status=status.HTTP_200_OK, data=devices)
        return Response(
            status=status.HTTP_200_OK, data={"message": "There is no device available."}
        )
