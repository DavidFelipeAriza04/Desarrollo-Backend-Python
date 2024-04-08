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


class TaskApiView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        data = [
            {
                "id": task.id,
                "description": task.description,
                "end_date": task.end_date,
                "project": task.project.name,
                "priority": task.priority,
            }
            for task in tasks
        ]

        return Response(data)

    def post(self, request):
        task = Task()
        task.description = request.data.get("description", "")
        enddate = request.data.get("end_date", "")
        task.end_date = datetime.strptime(enddate, "%d-%m-%YT%H:%M:%S")
        id_proyecto = request.data.get("project_id", "")
        task.project = Project.objects.get(id=id_proyecto)
        task.priority = request.data.get("priority", "")
        print(task)
        task.save()
        return Response({})

    def delete(self, request):
        id = request.data.get("id")
        task = Task.objects.get(id=id)
        task.delete()
        return Response({})

    def patch(self, request):
        id = request.data.get("id")
        task = Task.objects.get(id=id)
        task.description = request.data.get("description", task.description)
        task.end_date = request.data.get("end_date", task.end_date)
        task.project = Project.objects.get(
            id=request.data.get("project_id", task.project.id)
        )
        task.priority = request.data.get("priority", task.priority)
        task.save()
        return Response(
            {
                "id": task.id,
                "description": task.description,
                "end_date": task.end_date,
                "project": task.project.name,
                "priority": task.priority,
            }
        )
