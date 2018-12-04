from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from orm.models import Pekerja,Pko,Disiplin,Kesehatan,Psikotes,Petadua
from management.datapekerja.forms import PekerjaForm,PkoForm,DisiplinForm,KesehatanForm,PsikotesForm,PetaDuaForm
import mimetypes
import os




class ListDataPekerjaView(View):
    def get(self, request):
        pekerja = Pekerja.objects.all()
        template = 'datapekerja/index.html'
        data = {
            'pekerja' : pekerja,
        }
        return render(request, template, data)


class SaveDataPekerjaView(View):
    def post(self, request):        
        pekerja_form = PekerjaForm(request.POST or None, request.FILES)
        pko_form = PkoForm(request.POST or None)
        disiplin_form = DisiplinForm(request.POST or None)
        kesehatan_form = KesehatanForm(request.POST or None)
        psikotes_form = PsikotesForm(request.POST or None)
        petadua_form = PetaDuaForm(request.POST or None)

        if pekerja_form.is_valid() and pko_form.is_valid() and disiplin_form.is_valid() and kesehatan_form.is_valid() and psikotes_form.is_valid() and petadua_form.is_valid():
            
            pekerja = Pekerja()
            pekerja.nip= pekerja_form.cleaned_data['nip']
            pekerja.nama_ptp = pekerja_form.cleaned_data['nama_ptp']
            pekerja.nama = pekerja_form.cleaned_data['nama']
            pekerja.tgl_lahir= pekerja_form.cleaned_data['tgl_lahir']
            pekerja.alamat = pekerja_form.cleaned_data['alamat']
            pekerja.jenis_kelamin = pekerja_form.cleaned_data['jenis_kelamin']
            pekerja.agama = pekerja_form.cleaned_data['agama']
            pekerja.status = pekerja_form.cleaned_data['sttus']
            pekerja.save()

            pko = Pko()
            pko.pekerja = pekerja
            pko.jabatan = pko_form.cleaned_data['jabatan']  
            pko.nilai  = pko_form.cleaned_data['nilaipk']  
            pko.save()

            disiplin = Disiplin()
            disiplin.pekerja = pekerja
            disiplin.kehadiran = disiplin_form.cleaned_data['kehadiran']
            disiplin.pelanggaran = disiplin_form.cleaned_data['pelanggaran']
            disiplin.nilai = disiplin_form.cleaned_data['nilaidp']
            disiplin.save() 

            kesehatan = Kesehatan()
            kesehatan.pekerja = pekerja
            kesehatan.status_kes = kesehatan_form.cleaned_data['status_kes']      
            kesehatan.nilai = kesehatan_form.cleaned_data['nilaikh']      
            kesehatan.save()

            psikotes = Psikotes()
            psikotes.pekerja = pekerja
            psikotes.intelegensi = psikotes_form.cleaned_data['intelegensi']
            psikotes.kepribadian = psikotes_form.cleaned_data['kepribadian']
            psikotes.nilai = psikotes_form.cleaned_data['nilaipsk']
            psikotes.save()

            petadua = Petadua()
            petadua.pekerja  = pekerja
            petadua.teori = petadua_form.cleaned_data['teori']
            petadua.praktek = petadua_form.cleaned_data['praktek']
            petadua.nilai = petadua_form.cleaned_data['nilaipt2']
            petadua.save()
            messages.add_message(request, messages.INFO, 'Data Berhasil Disimpan')   

            return redirect('datapekerja:view')
        else:
            return HttpResponse(pekerja_form.errors and DisiplinForm.errors and PkoForm.errors and kesehatan_form.errors and psikotes_form.errors and petadua_form.errors)