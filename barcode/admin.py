from django.contrib import admin

from barcode.models import Setup


@admin.register(Setup)
class SetupAdmin(admin.ModelAdmin):
    list_display = ['organization_name', 'organization_location']
