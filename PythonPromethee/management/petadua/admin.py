from django.contrib import admin
from orm.models import Petadua

class PetaduaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Petadua, PetaduaAdmin)