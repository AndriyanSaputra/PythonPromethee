from django import forms
from orm.models import Pekerja,Pko,Disiplin,Kesehatan,Psikotes,Petadua
from django.contrib.auth.models import User

class PekerjaForm(forms.Form):
    nip = forms.IntegerField(initial=0)
    nama_ptp = forms.CharField(max_length=40)
    nama =  forms.CharField( max_length=30)
    tgl_lahir = forms.DateField(
        widget=forms.widgets.DateInput(format="%m/%d/%Y"))
    alamat = forms.CharField(max_length=200)
    jenis_kelamin = forms.CharField(max_length=30)
    agama = forms.CharField(max_length=30)
    status = forms.CharField(max_length=100)
    picture = forms.ImageField(initial="pekerja/profile/icon.png")

    class Meta:
        model = Pekerja

class PkoForm(forms.Form):
    jabatan = forms.CharField( max_length=30, required=False)
    nilai = forms.IntegerField(initial=0)

    class Meta:
        model = Pko

class DisiplinForm(forms.Form):
    kehadiran = forms.IntegerField(initial=0)
    pelanggaran = forms.IntegerField(initial=0)
    nilaidp = forms.IntegerField(initial=0)

    class Meta:
        model = Disiplin

class KesehatanForm(forms.Form):
    status_kes =forms.CharField(max_length=30, required=False)
    nilaikh = forms.IntegerField(initial=0)

    class Meta:
        model = Kesehatan

class PsikotesForm(forms.Form):
    intelegensi = forms.IntegerField(initial=0)
    kepribadian = forms.IntegerField(initial=0)
    nilaipsk = forms.IntegerField(initial=0)

    class Meta:
        model = Psikotes

class PetaduaForm(forms.Form):
    teori = forms.IntegerField(initial=0)
    praktek = forms.IntegerField(initial=0)
    nilaipt2 = forms.IntegerField(initial=0)

    class Meta:
        model = Petadua




