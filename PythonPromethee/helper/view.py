from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from braces import views


class ManagementAccessView(views.LoginRequiredMixin, views.SuperuserRequiredMixin, views.GroupRequiredMixin, generic.View):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    group_required = u"Administrator"

class PekerjaAccessView(views.LoginRequiredMixin, views.StaffuserRequiredMixin, views.GroupRequiredMixin, generic.View):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    group_required = u"Pekerja"
