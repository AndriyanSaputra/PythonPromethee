from django.contrib import admin
from orm.models import Calon

class CalonAdmin(admin.ModelAdmin):
    pass
admin.site.register(Calon, CalonAdmin)