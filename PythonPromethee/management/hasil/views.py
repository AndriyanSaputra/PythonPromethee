from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Pekerja,Pko,Disiplin,Kesehatan,Psikotes,Petadua
from management.hasil import helpers
from django.template.loader import get_template

# Create your views here.


class ListHasilView(View):
    def get(self, request):
        template = 'hasil/index.html'
        nl = helpers.rangking().as_matrix()
        data = {
            'hasil' : nl,
            
        }
        return render(request, template, data)