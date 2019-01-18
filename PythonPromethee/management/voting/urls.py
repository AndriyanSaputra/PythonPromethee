from django.conf.urls import url
from management.voting import views


urlpatterns = [
    url (r'^$', views.ListDataVotingView.as_view(), name='view'),
    url (r'^tonho$', views.sayatonho.as_view(), name='tonho'),
    # url (r'^add_calon$', views.AddCalonView.as_view(), name='add_calon'),
    # url (r'^save_calon$', views.SaveDataCalonView.as_view(), name='save_calon'),
    url (r'^hapus_pemilih/(?P<id>\d+)$', views.HapusDataPemilihView.as_view(), name='hapus_pemilih'),
    # url (r'^detail_calon/(?P<id>\d+)$', views.DetailDataCalonView.as_view(), name='detail_calon'),
    # url (r'^edit_calon/(?P<id>\d+)$', views.UbahCalonView.as_view(), name='edit_calon'),
    url (r'^update_calon/(?P<id>\d+)$', views.UpdateDataCalonView.as_view(), name='update_calon'),
]

   

