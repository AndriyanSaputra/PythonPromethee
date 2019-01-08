from django.contrib import admin
from orm.models import HakAkses

class HakAksesAdmin(admin.ModelAdmin):
    pass
admin.site.register(HakAkses, HakAksesAdmin)