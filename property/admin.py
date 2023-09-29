from django.contrib import admin

from .models import Flat


class FaltAdmin(admin.ModelAdmin):
    search_fields = ('owner', 'town', 'address')


admin.site.register(Flat,  FaltAdmin)
