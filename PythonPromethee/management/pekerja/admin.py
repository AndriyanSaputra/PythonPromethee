from django.contrib import admin
from orm.models import Pekerja

class PekerjaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Pekerja, PekerjaAdmin)