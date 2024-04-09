from django.contrib import admin

# Register your models here.
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "username"]

admin.site.register(user, UserAdmin)