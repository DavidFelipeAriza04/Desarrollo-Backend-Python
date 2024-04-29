from django.contrib import admin
from .models import *


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id","name", "init_date", "end_date")


class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "project", "description", "end_date")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "task", "content", "init_date")


class MemberAdmin(admin.ModelAdmin):
    list_display = ("id", "project", "user", "rol", "date_joined")


class OwnerAdmin(admin.ModelAdmin):
    list_display = ("id", "task", "user")


# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Owner, OwnerAdmin)
