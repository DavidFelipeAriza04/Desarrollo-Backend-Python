from django.urls import path, include
from .views import ProjectApiView, TaskApiView, ProjectViewSet, TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"projectsViewSet", ProjectViewSet, basename="projectsViewSet")
# router.register(r"projectsApiView", ProjectApiView.as_view(), basename="projectsApiView")
router.register(r"tasksViewSet", TaskViewSet, basename="tasksViewSet")
# router.register(r"tasksApiView", TaskApiView.as_view(), basename="tasksApiView")
urlpatterns = [
    path('projects/', ProjectApiView.as_view()),
    path('tasks/', TaskApiView.as_view()),
    path("", include(router.urls)),
]
