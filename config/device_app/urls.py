from django.urls import path
from .views import CreateDevice_API, GetDevice_API


urlpatterns = [
    path("devices/", CreateDevice_API.as_view(), name="create_device"),
    path("devices/id<pk>/", GetDevice_API.as_view(), name="get_device"),
]
