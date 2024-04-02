from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class user(AbstractUser):
    REQUIRED_FIELDS = ["email"]
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)

    def save(self,*args,**kwargs) -> None:
        self.username = self.email.split("@")[0]
        return super().save(*args,**kwargs)
