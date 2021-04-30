from django.contrib import admin

# Register your models here.
from .models import File,Folder,fav

admin.site.register(File)
admin.site.register(Folder)
admin.site.register(fav)