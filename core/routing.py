from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/projects/(?P<project_id>\d+)/$", consumers.TaskNotificationConsumer.as_asgi()),
]