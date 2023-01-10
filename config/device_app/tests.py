from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APISimpleTestCase

client = APIClient()


class TestGetDevice_API(APISimpleTestCase):
    """Test class for GetDevice_API endpoint view"""

    def test_case1_get_device_valid(self):
        response = client.get("http://127.0.0.1:8000/api/v1/devices/id1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_case2_get_device_invalid(self):
        response = client.get("http://127.0.0.1:8000/api/v1/devices/id567/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class Test_CreateDevice_API(APISimpleTestCase):
    """Test class for create a new Device using CreateDevice_API endpoint view"""

    def setUp(self):
        self.payload1_valid = {
            "id": "/devices/id5",
            "deviceModel": "/devicemodels/id5",
            "name": "Sensor5",
            "note": "Testing a sensor5.",
            "serial": "A020000105",
        }

        self.payload2_invalid = {
            "id": "",  # id required field
            "deviceModel": "/devicemodels/id2",
            "name": "",  # name required field
            "note": "Testing a sensor2.",
            # serial required field
        }

        self.payload3_invalid = {
            "id": "4",  # id format is invalid : must be in this format => /devices/id<pk>
            "deviceModel": "/devicemodels/id4",
            "name": "Sensor4",
            "note": "Testing a sensor4.",
            "serial": "A020000104",
        }

    def test_case1_create_device_valid(self):
        response = client.post(
            "http://127.0.0.1:8000/api/v1/devices/", self.payload1_valid
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_case2_create_device_invalid(self):
        response = client.post(
            "http://127.0.0.1:8000/api/v1/devices/", self.payload2_invalid
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_case3_create_device_invalid(self):
        response = client.post(
            "http://127.0.0.1:8000/api/v1/devices/", self.payload3_invalid
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_case4_create_device_invalide(self):
        response = client.post(
            "http://127.0.0.1:8000/api/v1/devices/", self.payload1_valid
        )
        self.assertEqual(
            response.status_code, status.HTTP_409_CONFLICT
        )  # item already exist
