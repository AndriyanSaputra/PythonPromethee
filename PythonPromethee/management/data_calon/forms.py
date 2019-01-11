from django import forms
from orm.models import Calon
from django.contrib.auth.models import User

class CalonForm(forms.Form):
	nip = forms.IntegerField(initial=0)
	nama = forms.CharField(max_length=100)
	nama_ptp =forms.CharField(max_length=100)
	visi = forms.CharField(max_length=100)
	misi = forms.CharField(max_length=100)
	picture = forms.ImageField()

		
	class Meta:
  		model = Calon
               
               