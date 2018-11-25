from django.conf.urls import url
from management.datapekerja import views


urlpatterns = [
    url (r'^$', views.ListDataAwalView.as_view(), name='view'),
    url (r'^save_data_pekeja$', views.SaveDataPekerjaView.as_view(), name='save_data_pekerja'),
 


]
