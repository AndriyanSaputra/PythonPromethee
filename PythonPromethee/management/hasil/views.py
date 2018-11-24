from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Pekerja,Pko,Disiplin,Kesehatan,Psikotes,Petadua
from management.hasil import helpers
from django.template.loader import get_template

# Create your views here.

pj=Pekerja.objects.all()
class ListDataAwalView(View):
    def get(self, request):
        template = 'hasil/dataawal.html'
        nl = helpers.dataawal(pj).as_matrix()
        data = {
            'dataawal' : nl,
            
        }
        return render(request, template, data)

class ListHasilView(View):
    def get(self, request):
        template = 'hasil/index.html'
        nl = helpers.rangking(pj).as_matrix()
        data = {
            'hasil' : nl,
            
        }
        return render(request, template, data)

class ListPrefPkoView(View):
    def get(self, request):
        template = 'hasil/prefpko.html'
        nl = helpers.krtpko(pj).as_matrix()
        data = {
            'prefpko' : nl,
            
        }
        return render(request, template, data)

class ListPrefDisiplinView(View):
    def get(self, request):
        template = 'hasil/prefdsp.html'
        nl = helpers.krtdsp(pj).as_matrix()
        data = {
            'prefdsp' : nl,
            
        }
        return render(request, template, data)


class ListPrefKesehatanView(View):
    def get(self, request):
        template = 'hasil/prefkes.html'
        nl = helpers.krtkes(pj).as_matrix()
        data = {
            'prefkes' : nl,
            
        }
        return render(request, template, data)


class ListPrefPsikotesView(View):
    def get(self, request):
        template = 'hasil/prefpsk.html'
        nl = helpers.krtpsk(pj).as_matrix()
        data = {
            'prefpsk' : nl,
            
        }
        return render(request, template, data)


class ListPrefPetaDuaView(View):
    def get(self, request):
        template = 'hasil/prefpt2.html'
        nl = helpers.krtpt2(pj).as_matrix()
        data = {
            'prefpt2' : nl,
            
        }
        return render(request, template, data)