from django.contrib import admin
from orm.models import Kesehatan

class KesehatanAdmin(admin.ModelAdmin):
    pass
admin.site.register(Kesehatan, KesehatanAdmin)