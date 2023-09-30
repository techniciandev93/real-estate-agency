from django.contrib import admin

from .models import Flat, Claim


class FaltAdmin(admin.ModelAdmin):
    search_fields = ('owner', 'town', 'address')
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'owners_phonenumber', 'owner_pure_phone', 'new_building', 'construction_year',
                    'town')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('like',)


class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')


admin.site.register(Flat,  FaltAdmin)
admin.site.register(Claim,  ClaimAdmin)
