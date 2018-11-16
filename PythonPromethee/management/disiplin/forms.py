from django import forms
from orm.models import Disiplin,Pekerja
# from django.contrib.auth.models import User


class DisiplinForm(forms.Form):
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    pekerja_all = Pekerja.objects.all()
    pekerja = forms.ModelChoiceField(queryset=pekerja_all, initial=0) 
    pelanggaran = forms.IntegerField(required=False, initial=0)
    nilai = forms.IntegerField( required=False, initial=0)
    kehadiran = forms.IntegerField( required=False, initial=0)
    
    
    # user = forms.CharField(User, initial=0)
    class Meta:
        model = Disiplin
