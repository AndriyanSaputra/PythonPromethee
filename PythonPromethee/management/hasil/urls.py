
from django.conf.urls import url
from management.hasil import views

urlpatterns = [
    url(r'^$', views.ListHasilView.as_view(), name='view'),
    url(r'^dataawal/$', views.ListDataAwalView.as_view(), name='dataawal'),
    url(r'^prefpko/$', views.ListPrefPkoView.as_view(), name='prefpko'),
    url(r'^prefdsp/$', views.ListPrefDisiplinView.as_view(), name='prefdsp'),
    url(r'^prefkes/$', views.ListPrefKesehatanView.as_view(), name='prefkes'),
    url(r'^prefpsk/$', views.ListPrefPsikotesView.as_view(), name='prefpsk'),
    url(r'^prefpt2/$', views.ListPrefPetaDuaView.as_view(), name='prefpt2'),
    url(r'^indpref/$', views.ListIndexPreferensiView.as_view(), name='indpref'),
 
 
]