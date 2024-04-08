from django.urls import path
from .views import ProjectApiView, TaskApiView
urlpatterns = [
    path('projects/', ProjectApiView.as_view()),
    path('tasks/', TaskApiView.as_view()),
]