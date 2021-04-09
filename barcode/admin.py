from django.contrib import admin

from barcode.models import Setup, Person


@admin.register(Setup)
class SetupAdmin(admin.ModelAdmin):
    list_display = ['organization_name', 'organization_location']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'code']
