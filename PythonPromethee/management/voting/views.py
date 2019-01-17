from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Pekerja,Pko,Disiplin,Kesehatan,Psikotes,Petadua, Calon, Pemilih
from management.hasil import helpers
from django.template.loader import get_template
from django.contrib.auth.mixins import LoginRequiredMixin   
from management.voting.forms import CalonForm
# from helper.views import PemilihAccessView
# Create your views here.

class ListDataVotingView(View):
    def get(self, request):
        template = 'voting/index.html'
        data = {
        
            'calon' : Calon.objects.all(),
            
        }
        return render(request, template, data)


class HapusDataPemilihView(View):
    def get(self, request, id):
        pemilih = Pemilih.objects.filter(id=id)
        if pemilih.exists():
            pemilih.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('data_pemilih:view')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!') 
            
class UpdateDataCalonView(View):
    def post(self, request, id):
        calon = Calon.objects.get(id=id)
        calon_form = CalonForm(request.POST or None, request.FILES)
        
        if calon_form.is_valid():   

            calon.score = calon_form.cleaned_data['score']
                    
            calon.save(force_update=True)
            messages.add_message(request, messages.INFO, 'Data Berhasil Diupdate')  

            return redirect('voting:view')
        else:
            return HttpResponse(calon_form.errors)
