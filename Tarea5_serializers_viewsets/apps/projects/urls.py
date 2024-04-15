from django.urls import path, include
from .views import ProjectApiView, TaskApiView, ProjectViewSet, TaskViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"projectsViewSet", ProjectViewSet, basename="projectsViewSet")
router.register(r"tasksViewSet", TaskViewSet, basename="tasksViewSet")
router.register(r"commentViewSet", CommentViewSet, basename="commentViewSet")
urlpatterns = [
    path("projects/", ProjectApiView.as_view()),
    path("tasks/", TaskApiView.as_view()),
    path("", include(router.urls)),
]
