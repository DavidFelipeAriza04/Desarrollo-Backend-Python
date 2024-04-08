from django.urls import path
from .views import ProjectApiView
urlpatterns = [
    path('projects/', ProjectApiView.as_view()),
]