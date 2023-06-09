from django.contrib import admin

from .models import Flat, Complaint, Owner


class Flat_ownersInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ["owner", "flat"]


@admin.register(Flat)
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


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ["flat"]


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ["name", "phonenumber", "pure_phone"]
    raw_id_fields = ["flats"]
    inlines = [
        Flat_ownersInline,
    ]
    exclude = ["flats"]
