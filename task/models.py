from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    Task = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    def __str__(self):
        return self.Task

    
