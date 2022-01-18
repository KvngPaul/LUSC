from django.contrib import admin

from .models import Driver

class DriverAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'fullName']
    ordering = ('first_name', 'last_name')
    filter_horiazontal = ()

    list_display = (
        'first_name',
        'last_name',
        'phone_number'
    )

    list_filter = (
        'first_name',
        'last_name',
    )

admin.site.register(Driver, DriverAdmin)
