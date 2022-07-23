from django.urls import path, re_path
from .views import CreateDevice_API, GetDevice_API


urlpatterns = [
    re_path(r"^devices/?$", CreateDevice_API.as_view(), name="create_device"),
    path("devices/id<pk>/", GetDevice_API.as_view(), name="get_device"),
]
