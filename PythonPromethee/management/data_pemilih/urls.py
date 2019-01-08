from django.conf.urls import url
from management.data_pemilih import views


urlpatterns = [
    url (r'^$', views.ListDataPemilihView.as_view(), name='view'),
    url (r'^save_pemilih$', views.SaveDataPemilihView.as_view(), name='save_pemilih'),
    url (r'^hapus_pemilih/(?P<id>\d+)$', views.HapusDataPemilihView.as_view(), name='hapus_pemilih'),
  	url (r'^detail_pemilih/(?P<id>\d+)$', views.DetailDataPemilihView.as_view(), name='detail_pemilih'),
  	url (r'^edit_pemilih/(?P<id>\d+)$', views.UbahPemilihView.as_view(), name='edit_pemilih'),
    url (r'^update_pemilih/(?P<id>\d+)$', views.UpdateDataPemilihView.as_view(), name='update_pemilih'),
 
    
    
   
]
