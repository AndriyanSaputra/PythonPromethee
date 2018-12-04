from django.conf.urls import url
from management.datapekerja import views


urlpatterns = [
    url (r'^$', views.ListDataPekerjaView.as_view(), name='view'),
    url (r'^save_pekerja$', views.SaveDataPekerjaView.as_view(), name='save_pekerja'),
 


]
