from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from orm.models import Pekerja
from login.forms import AuthenticateForm
from django.conf import settings
from login.forms import AuthenticateForm
from helper import authcheck
import pandas as pd
import requests


class LoginView(View):
    def get(self, request):
        template = 'login/login.html'
        form = AuthenticateForm(request.POST or None)
        data  = {
            'form': form,
        }
        return render(request, template, data)

class DoLoginView(View):
    def post(self, request):
        template = 'login.html'
        form = AuthenticateForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember = form.cleaned_data['remember']
            # ngecek user ada apa nggak
            user = authenticate(username=username, password=password) 
            if user is not None:
                # checkbox remember 
                print(user.is_staff)
                
                if not remember:
                    settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True
                    request.session.set_expiry(0)

                else:
                    settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False

                if authcheck.AuthCheck.isSuperUser(user):
                    login(request, user)
                    return redirect('data_pekerja:view')

                elif authcheck.AuthCheck.isPemilih(user):
                    login(request, user)
                    return redirect('voting:view')

                else:
                     messages.add_message(request, messages.WARNING,
                                 'Akun Belum Terdaftar Sebagai User !!')
            else:
                  messages.add_message(request, messages.WARNING,
                                 'Username dan atau Password tidak ditemukan !!')
        data  = {
            'form': form,
        }
        return redirect('login:view')

        
class DoLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login:view')
