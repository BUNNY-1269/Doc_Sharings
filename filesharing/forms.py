from django import forms
from .models import File,Folder

class DocumentForm(forms.ModelForm):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = File
        fields = ('file', )


class FolderForm(forms.ModelForm):
    name=forms.CharField(max_length=100)
    class Meta:
        model = Folder
        fields = ['name']


class FolderUploadForm(forms.ModelForm):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True, 'webkitdirectory': True, 'directory': True}))

    class Meta:
        model = File
        fields = ['file',]

