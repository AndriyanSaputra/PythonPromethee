from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from orm.models import Pemilih
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

class AddPemilihView(View):
    def get(self, request):
        template = 'data_pemilih/add_pemilih.html'
        pk = Pemilih.objects.all()
        
        # pekerja_form = PekerjaForm(request.POST or None, request.FILES)
        data = {
            'pemilih' : pk,
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
            pemilih.picture = pemilih_form.cleaned_data['picture']
            pemilih.save()

            

            messages.add_message(request, messages.INFO, 'Data Berhasil Disimpan')   

            return redirect('data_pemilih:view')
        else:
            return HttpResponse(pemilih_form.errors)

class HapusDataPemilihView(View):
    def get(self, request, id):
        pemilih = Pemilih.objects.filter(id=id)
        if pemilih.exists():
            pemilih.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('data_pemilih:view')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!') 

class DetailDataPemilihView(View):
    def get(self, request, id):
        template = 'data_pemilih/detail_pemilih.html'
        data = {
          'pemilih' : Pemilih.objects.get(id=id)
        }
        return render(request, template, data)

class UpdateDataPemilihView(View):
    def post(self, request, id):
        pemilih = Pemilih.objects.get(id=id)
        pemilih_form = PemilihForm(request.POST or None, request.FILES)
        user_form = UserForm(request.POST or None)

        if pemilih_form.is_valid() :

            if user_form.is_valid():
                user = pemilih.user
                user.username = user_form.cleaned_data['user']
                user.set_password(user_form.cleaned_data['password']) 
                user.save(force_update=True)
                # pekerja.user = user

            pemilih.user = user
            pemilih.nip = pemilih_form.cleaned_data['nip']
            pemilih.nama_ptp = pemilih_form.cleaned_data['nama_ptp']
            pemilih.nama = pemilih_form.cleaned_data['nama']
            pemilih.jenis_kelamin = pemilih_form.cleaned_data['jenis_kelamin']
            newpic = pemilih_form.cleaned_data.get('picture', None)

            if not newpic == None:
                    pemilih.picture = newpic
            pemilih.save(force_update=True)
            
           
            messages.add_message(request, messages.INFO, 'Data Berhasil Diupdate')  


            return redirect('data_pemilih:view')
        else:
            return HttpResponse(pemilih_form.errors)

class UbahPemilihView(View):
    def get(self, request, id):
        template = 'data_pemilih/edit_pemilih.html'
        data = {
            'pemilih': Pemilih.objects.get(id=id),
        }
        return render(request, template, data)

