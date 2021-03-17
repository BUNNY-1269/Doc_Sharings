from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import os
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)
# Create your models here.
class File(models.Model):

    name = models.CharField(max_length=100,null=True,blank=True)
    file=models.FileField(upload_to=user_directory_path);
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=None)
    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.name
    def delete(self, *args, **kwargs):
        self.file.delete()
        self.name.delete()
        super().delete(*args, **kwargs)
    
    
