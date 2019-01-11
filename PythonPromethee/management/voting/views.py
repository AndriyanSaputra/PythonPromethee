from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Pekerja,Pko,Disiplin,Kesehatan,Psikotes,Petadua
from management.hasil import helpers
from django.template.loader import get_template

# Create your views here.

class ListDataVotingView(View):
    def get(self, request):
        template = 'voting/index.html'
        data = {
            'dataawal' : Pekerja.objects.all(),
            
        }
        return render(request, template, data)