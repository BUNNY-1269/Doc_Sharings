from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import views as auth_views


# Create your models here.
class profile(models.Model):
    profilename = models.CharField(max_length=100)
    DOB = models.DateField()
    college = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='profilepic')
    owner=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.profilename