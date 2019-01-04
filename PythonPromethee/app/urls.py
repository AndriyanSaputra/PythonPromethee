"""PythonPromethee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from app.config import setting
from login import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('login.urls', namespace='login')),
    # url(r'^pekerja/', include('pekerja.urls', namespace='pekerja')),
    url(r'^hasil/', include('management.hasil.urls', namespace='hasil')),
    url(r'^datapekerja/', include('management.data_pekerja.urls', namespace='data_pekerja')),
    url(r'^datapemilih/', include('management.data_pemilih.urls', namespace='data_pemilih')),
    # url(r'^bobot/', include('management.bobot.urls', namespace='bobot')),
]

urlpatterns +=  staticfiles_urlpatterns()
urlpatterns += static(setting.MEDIA_URL, document_root=setting.MEDIA_ROOT)