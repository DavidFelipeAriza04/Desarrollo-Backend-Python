from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

# self modules
from .models import *

# utils
from datetime import datetime


class ProjectApiView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        data = [{"id": project.id, "name": project.name} for project in projects]

        return Response(data)

    def post(self, request):
        project = Project()
        project.name = request.data.get("name", "")
        project.init_date = datetime.now()
        enddate = request.data.get("end_date", "")
        project.end_date = datetime.strptime(enddate, "%d-%m-%YT%H:%M:%S")
        print(project)
        project.save()
        return Response({})

    def delete(self, request):
        id = request.data.get("id")
        project = Project.objects.get(id=id)
        project = Project.objects.get(id=request.data.get("id", ""))
        project.delete()
        return Response({})

    def patch(self, request):
        id = request.data.get("id")
        project = Project.objects.get(id=id)
        project.name = request.data.get("name", project.name)
        project.save()
        return Response({"id": project.id, "name": project.name})