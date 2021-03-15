from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import os

# Create your models here.
class File(models.Model):

    name = models.CharField(max_length=100,null=True,blank=True)
    file=models.FileField();
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name