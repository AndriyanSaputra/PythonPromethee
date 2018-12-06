from django.conf.urls import url
from management.databuruh import views


urlpatterns = [
    url (r'^$', views.ListDataBuruhView.as_view(), name='view'),
    url (r'^save_buruh$', views.SaveDataBuruhView.as_view(), name='save_buruh'),
    url (r'^hapus_data_buruh/(?P<id>\d+)$', views.HapusDataBuruhView.as_view(), name='hapus_data_buruh'),


]
