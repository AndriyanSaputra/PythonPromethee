from django import forms
from orm.models import Calon
from django.contrib.auth.models import User

class CalonForm(forms.Form):
    score = forms.IntegerField(initial=0)
        
    class Meta:
        model = Calon
               
               