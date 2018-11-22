
from django.conf.urls import url
from management.hasil import views

urlpatterns = [
    url (r'^$', views.ListHasilView.as_view(), name='view'),
 
]