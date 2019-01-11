from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from orm.models import Calon
from management.data_calon.forms import CalonForm
from django.contrib.auth.models import User 
import mimetypes
import os

class ListDataCalonView(View):
    def get(self, request):
        pk = Calon.objects.all()
        template = 'data_calon/calon.html'
        data = {
            'calon' : pk,
        }
        return render(request, template, data)

class AddCalonView(View):
    def get(self, request):
        template = 'data_calon/add_calon.html'
        pk = Calon.objects.all()
        
        # pekerja_form = PekerjaForm(request.POST or None, request.FILES)
        data = {
            'calon' : pk,
        }
        return render(request, template, data)


class SaveDataCalonView(View):
    def post(self, request):
        calon_form = CalonForm(request.POST or None, request.FILES)
        

        if calon_form.is_valid():

            calon = Calon()
            calon.nama_ketua = calon_form.cleaned_data['nama_ketua']
            calon.nama_wakil = calon_form.cleaned_data['nama_wakil']
            calon.visi = calon_form.cleaned_data['visi']
            calon.misi = calon_form.cleaned_data['misi']
            calon.picture = calon_form.cleaned_data['picture']
            calon.picture2 = calon_form.cleaned_data['picture2']
            calon.save()


            messages.add_message(request, messages.INFO, 'Data Berhasil Disimpan')   

            return redirect('data_calon:view')
        else:
            return HttpResponse(calon_form.errors)

class HapusDataCalonView(View):
    def get(self, request, id):
        calon = Calon.objects.filter(id=id)
        if calon.exists():
            calon.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('data_calon:view')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!') 

class UbahCalonView(View):
    def get(self, request, id):
        template = 'data_calon/edit_calon.html'
        data = {
            'calon': Calon.objects.get(id=id),
        }
        return render(request, template, data)


class UpdateDataCalonView(View):
    def post(self, request, id):
        calon = Calon.objects.get(id=id)
        calon_form = CalonForm(request.POST or None, request.FILES)
        
        if calon_form.is_valid():

                # pekerja.user = user

            calon.nama_ketua = calon_form.cleaned_data['nama_ketua']
            calon.nama_wakil = calon_form.cleaned_data['nama_wakil']
            calon.visi = calon_form.cleaned_data['visi']
            calon.misi= calon_form.cleaned_data['misi']
            newpic = calon_form.cleaned_data.get('picture', None)

            if not newpic == None:
                    calon.picture = newpic
                    
            newpic2 = calon_form.cleaned_data.get('picture2', None)

            if not newpic == None:
                    calon.picture2 = newpic2
                    
            calon.save(force_update=True)
            messages.add_message(request, messages.INFO, 'Data Berhasil Diupdate')  

            return redirect('data_calon:view')
        else:
            return HttpResponse(calon_form.errors)

class DetailDataCalonView(View):
    def get(self, request, id):
        template = 'data_calon/detail_calon.html'
        data = {
          'calon' : Calon.objects.get(id=id)
        }
        return render(request, template, data)


