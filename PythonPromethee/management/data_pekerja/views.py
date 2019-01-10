from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from orm.models import Pekerja,Pko,Disiplin,Kesehatan,Psikotes,Petadua
from management.data_pekerja.forms import PekerjaForm,PkoForm,DisiplinForm,KesehatanForm,PsikotesForm,PetaduaForm,UserForm
from django.contrib.auth.models import User 
import mimetypes
import os



class ListDataPekerjaView(View):
    def get(self, request):
        pk = Pekerja.objects.all()
        template = 'data_pekerja/index.html'
        data = {
            'pekerja' : pk,
        }
        return render(request, template, data)

class SaveDataPekerjaView(View):
    def post(self, request):
        pekerja_form = PekerjaForm(request.POST or None, request.FILES)
        pko_form = PkoForm(request.POST or None)
        disiplin_form = DisiplinForm(request.POST or None)
        kesehatan_form = KesehatanForm(request.POST or None)
        psikotes_form = PsikotesForm(request.POST or None)
        petadua_form = PetaduaForm(request.POST or None)


        if pekerja_form.is_valid() and pko_form.is_valid() and disiplin_form.is_valid() and kesehatan_form.is_valid() and psikotes_form.is_valid() and petadua_form.is_valid():
            
            user = User()
            user.username = request.POST['username']
            user.set_password(request.POST['password'])
            staff = request.POST.get('staff', None)
            if not staff == None:
                user.is_staff = True
                user.save()

            else:
                user.save()

            pekerja = Pekerja()
            pekerja.user = user
            pekerja.nip = pekerja_form.cleaned_data['nip']
            pekerja.nama_ptp = pekerja_form.cleaned_data['nama_ptp']
            pekerja.nama = pekerja_form.cleaned_data['nama']
            pekerja.tgl_lahir = pekerja_form.cleaned_data['tgl_lahir']
            pekerja.alamat = pekerja_form.cleaned_data['alamat']
            pekerja.jenis_kelamin = pekerja_form.cleaned_data['jenis_kelamin']
            pekerja.agama = pekerja_form.cleaned_data['agama']
            pekerja.status = pekerja_form.cleaned_data['status']
            pekerja.gambar = pekerja_form.cleaned_data['gambar']
            pekerja.save()

            pko = Pko()
            pko.pekerja = pekerja
            pko.jabatan = pko_form.cleaned_data['jabatan']
            pko.nilai = pko_form.cleaned_data['nilai']
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
            petadua.pekerja = pekerja
            petadua.praktek = petadua_form.cleaned_data['praktek']
            petadua.teori = petadua_form.cleaned_data['teori']
            petadua.nilai = petadua_form.cleaned_data['nilaipt2']
            petadua.save()

            messages.add_message(request, messages.INFO, 'Data Berhasil Disimpan')   

            return redirect('data_pekerja:view')
        else:
            return HttpResponse(pekerja_form.errors and pko_form.errors and disiplin_form.errors and kesehatan_form.errors and psikotes_form.errors and petadua_form.errors)


class HapusDataPekerjaView(View):
    def get(self, request, id):
        pekerja = Pekerja.objects.filter(id=id)
        if pekerja.exists():
            pekerja.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('data_pekerja:view')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!') 


class UpdateDataPekerjaView(View):
    def post(self, request, id):
        pekerja = Pekerja.objects.get(id=id)
        pekerja_form = PekerjaForm(request.POST or None, request.FILES)
        pko_form = PkoForm(request.POST or None)
        disiplin_form = DisiplinForm(request.POST or None)
        kesehatan_form = KesehatanForm(request.POST or None)
        psikotes_form = PsikotesForm(request.POST or None)
        petadua_form = PetaduaForm(request.POST or None)
        user_form = UserForm(request.POST or None)

        if pekerja_form.is_valid() and pko_form.is_valid() and disiplin_form.is_valid() and kesehatan_form.is_valid() and psikotes_form.is_valid() and petadua_form.is_valid():

            if user_form.is_valid():
                user = pekerja.user
                user.username = user_form.cleaned_data['user']
                user.set_password(user_form.cleaned_data['password']) 
                user.save(force_update=True)
                # pekerja.user = user

            pekerja.user = user
            pekerja.nip = pekerja_form.cleaned_data['nip']
            pekerja.nama_ptp = pekerja_form.cleaned_data['nama_ptp']
            pekerja.nama = pekerja_form.cleaned_data['nama']
            pekerja.tgl_lahir = pekerja_form.cleaned_data['tgl_lahir']
            pekerja.alamat = pekerja_form.cleaned_data['alamat']
            pekerja.jenis_kelamin = pekerja_form.cleaned_data['jenis_kelamin']
            pekerja.agama = pekerja_form.cleaned_data['agama']
            pekerja.status = pekerja_form.cleaned_data['status']
            newpic = pekerja_form.cleaned_data.get('gambar', None)

            if not newpic == None:
                    pekerja.gambar = newpic
                    
            pekerja.save(force_update=True)
            
            pekerja.Pkos.pekerja = pekerja
            pekerja.Pkos.jabatan = pko_form.cleaned_data['jabatan']
            pekerja.Pkos.nilai = pko_form.cleaned_data['nilai']
            pekerja.Pkos.save(force_update=True)

            pekerja.Disiplins.pekerja = pekerja
            pekerja.Disiplins.kehadiran = disiplin_form.cleaned_data['kehadiran']
            pekerja.Disiplins.pelanggaran = disiplin_form.cleaned_data['pelanggaran']
            pekerja.Disiplins.nilai = disiplin_form.cleaned_data['nilaidp']
            pekerja.Disiplins.save(force_update=True) 

            pekerja.Kesehatans.pekerja = pekerja
            pekerja.Kesehatans.status_kes = kesehatan_form.cleaned_data['status_kes']
            pekerja.Kesehatans.nilai = kesehatan_form.cleaned_data['nilaikh']
            pekerja.Kesehatans.save(force_update=True)

            pekerja.Psikotess.pekerja = pekerja
            pekerja.Psikotess.intelegensi = psikotes_form.cleaned_data['intelegensi']
            pekerja.Psikotess.kepribadian = psikotes_form.cleaned_data['kepribadian']
            pekerja.Psikotess.nilai = psikotes_form.cleaned_data['nilaipsk']
            pekerja.Psikotess.save(force_update=True)

            pekerja.Petaduas.pekerja = pekerja
            pekerja.Petaduas.teori = petadua_form.cleaned_data['teori']
            pekerja.Petaduas.praktek = petadua_form.cleaned_data['praktek']
            pekerja.Petaduas.nilai = petadua_form.cleaned_data['nilaipt2']
            pekerja.Petaduas.save(force_update=True)
            messages.add_message(request, messages.INFO, 'Data Berhasil Diupdate')  


            return redirect('data_pekerja:view')
        else:
            return HttpResponse(pekerja_form.errors and pko_form.errors and disiplin_form.errors and kesehatan_form.errors and psikotes_form.errors and petadua_form.errors)

class DetailDataPekerjaView(View):
    def get(self, request, id):
        template = 'data_pekerja/detail_pekerja.html'
        data = {
          'pekerja' : Pekerja.objects.get(id=id)
        }
        return render(request, template, data)

class UbahPekerjaView(View):
    def get(self, request, id):
        template = 'data_pekerja/edit_pekerja.html'
        data = {
            'pekerja': Pekerja.objects.get(id=id),
        }
        return render(request, template, data)


