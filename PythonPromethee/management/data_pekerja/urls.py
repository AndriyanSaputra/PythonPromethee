from django.conf.urls import url
from management.data_pekerja import views


urlpatterns = [
    url (r'^$', views.ListDataPekerjaView.as_view(), name='view'),
    url (r'^save_pekerja$', views.SaveDataPekerjaView.as_view(), name='save_pekerja'),
    url (r'^hapus_data_pekerja/(?P<id>\d+)$', views.HapusDataPekerjaView.as_view(), name='hapus_data_pekerja'),
    url (r'^detail_pekerja/(?P<id>\d+)$', views.DetailDataPekerjaView.as_view(), name='detail_pekerja'),
    url (r'^edit_pekerja/(?P<id>\d+)$', views.UbahDataPekerjaView.as_view(), name='edit_pekerja'),
    url (r'^update_pekerja/(?P<id>\d+)$', views.UpdateDataPekerjaView.as_view(), name='update_pekerja'),
]
