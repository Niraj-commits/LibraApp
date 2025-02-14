from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    role_choices = [('admin','admin'),('member','member')]

    role = models.CharField(max_length=50,choices=role_choices,default='member')
    def __str__(self):
        return f"{self.username} ({self.role})" 