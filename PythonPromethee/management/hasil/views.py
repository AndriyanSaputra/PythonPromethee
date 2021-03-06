from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Pekerja,Pko,Disiplin,Kesehatan,Psikotes,Petadua
from management.hasil import helpers
from django.template.loader import get_template

# Create your views here.

class ListDataAwalView(View):
    def get(self, request):
        template = 'hasil/dataawal.html'
        data = {
            'dataawal' : Pekerja.objects.all(),
            
        }
        return render(request, template, data)

class ListHasilView(View):
    def get(self, request):
        template = 'hasil/index.html'
        pj=Pekerja.objects.all()
        nl = helpers.rangking(pj).as_matrix()
        data = {
            'hasil' : nl,
            
        }
        return render(request, template, data)

class ListPrefPkoView(View):
    def get(self, request):
        template = 'hasil/prefpko.html'
        pj=Pekerja.objects.all()        
        nl = helpers.krtpko(pj).as_matrix()
        data = {
            'prefpko' : nl,
            
        }
        return render(request, template, data)

class ListPrefDisiplinView(View):
    def get(self, request):
        template = 'hasil/prefdsp.html'
        pj=Pekerja.objects.all()
        nl = helpers.krtdsp(pj).as_matrix()
        data = {
            'prefdsp' : nl,
            
        }
        return render(request, template, data)


class ListPrefKesehatanView(View):
    def get(self, request):
        template = 'hasil/prefkes.html'
        pj=Pekerja.objects.all()
        nl = helpers.krtkes(pj).as_matrix()
        data = {
            'prefkes' : nl,
            
        }
        return render(request, template, data)


class ListPrefPsikotesView(View):
    def get(self, request):
        template = 'hasil/prefpsk.html'
        pj=Pekerja.objects.all()

        nl = helpers.krtpsk(pj).as_matrix()
        data = {
            'prefpsk' : nl,
            
        }
        return render(request, template, data)


class ListPrefPetaDuaView(View):
    def get(self, request):
        template = 'hasil/prefpt2.html'
        pj=Pekerja.objects.all()

        nl = helpers.krtpt2(pj).as_matrix()
        data = {
            'prefpt2' : nl,
            
        }
        return render(request, template, data)

class ListIndexPreferensiView(View):
    def get(self, request):
        template = 'hasil/indpref.html'
        pj=Pekerja.objects.all()

        nl = helpers.dfindpref(pj).as_matrix()
        data = {
            'indpref' : nl,
            
        }
        return render(request, template, data)

class ListVoteView(View):
    def get(self, request):
        template = 'hasil/voting.html'
        pj=Pekerja.objects.all()
        nl = helpers.dfindpref(pj).as_matrix()
        data = {
            # 'vote' : vote,
            
        }
        return render(request, template, data)
        

