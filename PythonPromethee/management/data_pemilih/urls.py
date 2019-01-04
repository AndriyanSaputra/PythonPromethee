from django.conf.urls import url
from management.data_pemilih import views


urlpatterns = [
    url (r'^$', views.ListDataPemilihView.as_view(), name='view'),
    url (r'^save_pemilih$', views.SaveDataPemilihView.as_view(), name='save_pemilih'),
    url (r'^hapus_pemilih$', views.HapusDataPemilihView.as_view(), name='hapus_pemilih'),
    
   
]
