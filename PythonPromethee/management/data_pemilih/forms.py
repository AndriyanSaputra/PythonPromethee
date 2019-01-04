from django import forms
from orm.models import Pekerja,Pemilih
from django.contrib.auth.models import User


class UserForm(forms.Form):
    user = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = User

class PemilihForm(forms.Form):
	user = forms.CharField(max_length=100)
	nip = forms.IntegerField(initial=0)
	nama = forms.CharField(max_length=100)
	nama_ptp =forms.CharField(max_length=100)
	jenis_kelamin = forms.CharField(max_length=30)
		
	class Meta:
  		model = Pemilih