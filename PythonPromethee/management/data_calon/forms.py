from django import forms
from orm.models import Calon
from django.contrib.auth.models import User

class CalonForm(forms.Form):
	nama_ketua = forms.CharField(max_length=100)
	nama_wakil = forms.CharField(max_length=100)
	visi = forms.CharField(max_length=100)
	misi = forms.CharField(max_length=100)
	picture = forms.ImageField()
	picture2 = forms.ImageField()

		
	class Meta:
  		model = Calon
               
               