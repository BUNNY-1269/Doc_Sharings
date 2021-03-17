from django import forms
from .models import profile

class imageform(forms.ModelForm):

    class Meta:
        model = profile
        fields = ('image','profilename', )

class profilecreate(forms.ModelForm):

    class Meta:
        model = profile
        fields = ('image','profilename','DOB','college' )