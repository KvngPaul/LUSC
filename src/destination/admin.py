from django.contrib import admin

from .models import (
    Destination,
    DestinationLink,
)

class DestinationAdmin(admin.ModelAdmin):
    search_fields = ['town', 'area']
    ordering = ('town',)
    filter_horizontal = ()

    list_display = (
        'town',
        'area',
    )

    list_filter = (
        'town',
    )

admin.site.register(Destination, DestinationAdmin)
admin.site.register(DestinationLink)