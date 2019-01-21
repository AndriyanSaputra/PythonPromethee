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
    url(r'^hasil/', include('management.hasil.urls', namespace='hasil')),
    url(r'^datapekerja/', include('management.data_pekerja.urls', namespace='data_pekerja')),
    url(r'^datapemilih/', include('management.data_pemilih.urls', namespace='data_pemilih')),
    url(r'^data_calon/', include('management.data_calon.urls', namespace='data_calon')),
    url(r'^voting/', include('management.voting.urls', namespace='voting')),
    # url(r'^data_user/', include('data_user.urls', namespace='data_user')),
]

urlpatterns +=  staticfiles_urlpatterns()
urlpatterns += static(setting.MEDIA_URL, document_root=setting.MEDIA_ROOT)