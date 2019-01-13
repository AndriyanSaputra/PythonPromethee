from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Pekerja,Pko,Disiplin,Kesehatan,Psikotes,Petadua, Calon, Pemilih
from management.hasil import helpers
from django.template.loader import get_template
from django.contrib.auth.mixins import LoginRequiredMixin   
# from helper.views import PemilihAccessView
# Create your views here.

class ListDataVotingView(View):
    def get(self, request):
        template = 'voting/index.html'
        data = {
            'calon' : Calon.objects.all(),
            
        }
        return render(request, template, data)

# class PemiluView(View):
#     def get(self , request , id):
#         pilih = Pemilih.objects.get(id=id) + 1
#         data = {
#             'data_pemilih' : pilih
#         }

#         if Calon.is_valid():
#             calon = Calon()
#             calon.score = pilih.cleaned_data['score']
#             calon.save()

#             messages.add_message(request, messages.INFO, 'Anda Sudah Memilih Calon Tersebut')  

            # return redirect()


