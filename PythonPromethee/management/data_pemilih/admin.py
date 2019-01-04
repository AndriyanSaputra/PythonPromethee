from django.contrib import admin
from orm.models import Pemilih

class PemilihAdmin(admin.ModelAdmin):
    pass
admin.site.register(Pemilih, PemilihAdmin)