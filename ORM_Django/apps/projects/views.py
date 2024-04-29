from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


# self modules
from .models import *
from .serializers import ProjectSerializerModel, ProjectSerializer, TaskSerializerModel, TaskDetailSerializer
from .permissions import IsMemberOrOwner

# utils
from datetime import datetime


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializerModel
    permission_classes = [IsAuthenticated]


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializerModel
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["project"]

    def get_permissions(self):
        if self.action == "create":
            return super().get_permissions() + [IsMemberOrOwner()]
        return super().get_permissions()
    
    def get_serializer_class(self):
        if self.request.query_params.get("detail", False):
            return TaskDetailSerializer
        return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        print(self.request.user, "<-->")
        return super().list(request, *args, **kwargs)

    def filter_queryset(self, queryset):
        request_user = self.request.user
        queryset = super().filter_queryset(queryset)
        queryset = queryset.filter(owner__user=request_user)
        return queryset

    @action(detail=True, methods=["post"])
    def complete_task(self, request, pk=None):
        task = self.get_object()
        task.is_completed = True
        task.save()
        task_data = self.get_serializer_class()(task).data
        return Response(task_data)


# YA NO ES NECESARIO LOS API VIEWS
class ProjectApiView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        # data = [{"id": project.id, "name": project.name} for project in projects]
        # return Response(data)

        serializer = ProjectSerializer(projects, many=True)

        return Response(serializer.data)

    def post(self, request):
        project = Project()
        # project.name = request.data.get("name", "")
        # project.init_date = datetime.now()
        # enddate = request.data.get("end_date", "")
        # project.end_date = datetime.strptime(enddate, "%d-%m-%YT%H:%M:%S")
        # print(project)
        # project.save()
        # return Response({})
        serializer = ProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

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
