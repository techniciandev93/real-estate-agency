from django.contrib import admin
from .models import Flat, Claim, Owner


class OwnerAdminInline(admin.TabularInline):
    model = Owner.owner_apartments.through
    raw_id_fields = ('owner',)


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year',
                    'town')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('like',)
    inlines = [OwnerAdminInline]


class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('owner_apartments',)


admin.site.register(Flat,  FlatAdmin)
admin.site.register(Claim,  ClaimAdmin)
admin.site.register(Owner,  OwnerAdmin)
