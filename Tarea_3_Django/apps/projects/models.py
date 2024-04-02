from django.db import models

# Imports From Other Apps
from apps.users.models import user


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    init_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=False, blank=False)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    description = models.CharField(max_length=250, null=False, blank=False)
    end_date = models.DateTimeField(null=False, blank=False)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)

    Prioridades = {"Baja": "Baja", "Media": "Media", "Alta": "Alta"}
    priority = models.CharField(max_length=5, choices=Prioridades.items(),default='Media', null=False, blank=False)


class Comment(models.Model):
    init_date = models.DateTimeField(null=False, blank=False)
    content = models.CharField(max_length=120, null=False, blank=False)
    task = models.ForeignKey(Task, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(user, on_delete=models.DO_NOTHING)

class Member(models.Model):
    user = models.ForeignKey(user, on_delete=models.DO_NOTHING)
    Project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    roles = {
        "Admin": "Admin",
        "Developer": "Developer",
        "Manager": "Manager",
        "Client": "Client",
    }
    rol = models.CharField(max_length=10, choices=roles.items(), default="Developer", null=False, blank=False)
    date = models.DateTimeField(null=False, blank=False)

class Owner(models.Model):
    user = models.ForeignKey(user, on_delete=models.DO_NOTHING)
    task = models.ForeignKey(Task, on_delete=models.DO_NOTHING)