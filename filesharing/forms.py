from django import forms
from .models import File

class DocumentForm(forms.ModelForm):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': False}))
    class Meta:
        model = File
        fields = ('file', )
