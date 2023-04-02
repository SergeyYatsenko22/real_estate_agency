from django.contrib import admin

from .models import Flat, Complaint, Owner


class Flat_ownersInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ["owner", "flat"]


class FlatAdmin(admin.ModelAdmin):
    search_fields = ["town", "address"]
    readonly_fields = ["created_at"]
    list_display = ["address", "price", "new_building", "town"]
    list_editable = ["new_building"]
    list_filter = ["new_building", "town", "construction_year"]
    raw_id_fields = ["likes"]
    inlines = [
        Flat_ownersInline,
    ]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ["complaint"]


class OwnerAdmin(admin.ModelAdmin):
    list_display = ["owner_name", "owners_phonenumber", "owner_pure_phone"]
    raw_id_fields = ["flats"]
    inlines = [
        Flat_ownersInline,
    ]
    exclude = ["flats"]


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
