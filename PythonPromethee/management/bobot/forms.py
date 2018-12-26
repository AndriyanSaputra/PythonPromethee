from django import forms
from orm.models import Bobot
# from django.contrib.auth.models import User


class BobotForm(forms.Form):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    pko = forms.IntegerField( required=False, initial=0)
    disiplin = forms.IntegerField( required=False, initial=0)
    kesehatan = forms.IntegerField( required=False, initial=0)
    psikotes = forms.IntegerField( required=False, initial=0)
    petadua = forms.IntegerField( required=False, initial=0)
    
    
    # user = forms.CharField(User, initial=0)
    class Meta:
        model = Bobot


