from django.contrib import admin
from orm.models import Pko

class PkoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Pko, PkoAdmin)