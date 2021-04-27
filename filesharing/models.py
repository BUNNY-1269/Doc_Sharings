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
    folder=models.ForeignKey(Folder,null=True,on_delete=models.CASCADE,blank=True)
    isprivate = models.BooleanField(default=False)
    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        file=File.objects.get(pk=self.pk)
        folders=file.folder
        if not folder :
            return reverse('filesharing:index')
        else :
            return reverse('filesharing:detail',kwargs={'folder_id':folders.pk})

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

class Folder(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE, default=None)
    linkedfolder=models.ForeignKey("self",null=true,on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return  self.name

    def get_absolute_url(self):
        return reverse('fileshare:index')
