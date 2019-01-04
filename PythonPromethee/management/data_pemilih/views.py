from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from orm.models import Pekerja,Pemilih
from management.data_pemilih.forms import UserForm,PemilihForm
from django.contrib.auth.models import User 
import mimetypes
import os

class ListDataPemilihView(View):
    def get(self, request):
        pl = Pemilih.objects.all()
        template = 'data_pemilih/pemilih.html'
        data = {
        	'pemilih' : pl,
           
        }
        return render(request, template, data)

class SaveDataPemilihView(View):
    def post(self, request):
        pemilih_form = PemilihForm(request.POST or None, request.FILES)
        # pekerja_form = pekerja_form(request.POST or None, request.FILES)
        if pemilih_form.is_valid():
            
            user = User()
            user.username= request.POST['user']
            user.set_password(request.POST['password'])
            staff = request.POST.get('staff', None)
            if not staff == None:
                user.is_staff = True
                user.save()

            else:
                user.save()
            # pekerja = Pekerja()
            pemilih = Pemilih()
            pemilih.user = user
            pemilih.nip = pemilih_form.cleaned_data['nip']
            pemilih.nama_ptp = pemilih_form.cleaned_data['nama_ptp']
            pemilih.nama = pemilih_form.cleaned_data['nama']
            pemilih.jenis_kelamin = pemilih_form.cleaned_data['jenis_kelamin']
            pemilih.save()

            

            messages.add_message(request, messages.INFO, 'Data Berhasil Disimpan')   

            return redirect('data_pemilih:view')
        else:
            return HttpResponse(pemilih_form.errors)

class HapusDataPemilihView(View):
    def get(self, request, id):
        pemilih = Pekerja.objects.filter(id=id)
        if pemilih.exists():
            pemilih.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('data_pemilih:view')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!') 



