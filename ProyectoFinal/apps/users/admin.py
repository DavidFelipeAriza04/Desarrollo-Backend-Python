from django.contrib import admin

from .models import User

# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'email')

admin.site.register(User, UsersAdmin)