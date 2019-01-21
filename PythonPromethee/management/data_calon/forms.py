from django import forms
from orm.models import Calon
from django.contrib.auth.models import User

class CalonForm(forms.Form):
	nama_calon = forms.CharField(max_length=100)
	visi = forms.CharField(max_length=100)
	misi = forms.CharField(max_length=100)
	picture = forms.ImageField(initial="pemilih/profile/icon.png")

		
	class Meta:
  		model = Calon
               
               