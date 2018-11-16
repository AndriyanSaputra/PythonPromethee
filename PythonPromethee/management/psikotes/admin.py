from django.contrib import admin
from orm.models import Psikotes

class PsikotesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Psikotes, PsikotesAdmin)