from django.contrib import admin
from orm.models import Disiplin

class DisiplinAdmin(admin.ModelAdmin):
    pass
admin.site.register(Disiplin, DisiplinAdmin)