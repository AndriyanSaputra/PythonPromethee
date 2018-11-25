from django import forms
from orm.models import Pekerja,Pko,Disiplin,Kesehatan,Psikotes,Petadua
from django.contrib.auth.models import User



class PekerjaForm(forms.Form):
    nip = forms.CharField( max_length=50, required=False)
    nama_ptp = forms.CharField(max_length=30)
    nama = forms.CharField( max_length=30, required=False)
    tanggal_lahir= forms.DateField(
        widget=forms.widgets.DateInput(format="%m/%d/%Y"))
    jenis_kelamin = forms.CharField(max_length=30)
    alamat = forms.CharField(max_length=70)
    agama = forms.CharField(max_length=80, required=False)
    status = forms.CharField( max_length=40, required=False)

    class Meta:
        model = Pekerja

class PkoForm(forms.Form):
    jabatan = forms.CharField(max_length=50)
    nilaipko = forms.IntegerField(initial=0)
    
    class Meta:
        model = Pko

class DisiplinForm(forms.Form):
    kehadiaran = forms.IntegerField(required=False)
    pelanggaran = forms.IntegerField(required=False)
    nilaidsp = forms.IntegerField(initial=0)
    
    class Meta:
        model = Disiplin

class KesehatanForm(forms.Form):
    keterangan = forms.CharField(max_length=30)
    nilaikes = forms.IntegerField(initial=0)
    
    class Meta:
        model = Kesehatan

class PsikotesForm(forms.Form):
    intelegensi  = forms.CharField(max_length=30)
    kepribadian = forms.CharField(max_length=30, required=False)
    nilaipsk = forms.IntegerField(initial=0)
    
    class Meta:
        model = Psikotes

class PetaDuaForm(forms.Form):
    teori  = forms.CharField(max_length=30)
    praktek = forms.CharField(max_length=30, required=False)
    nilaipt2 = forms.IntegerField(initial=0)
    
    class Meta:
        model = Petadua
