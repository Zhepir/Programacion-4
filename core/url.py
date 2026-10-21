from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

from core.views import RegisterView, SocialLoginJWTView


router = DefaultRouter()

router.register(r"projects", views.ProjectViewSet, basename="project")
router.register(r"tasks", views.TaskViewSet, basename="task")


urlpatterns = [
    path("", include(router.urls)),
]