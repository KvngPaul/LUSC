from django.contrib import admin

from .models import (
    State,
    Town
)

class StateAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ('name',)
    filter_horizontal = ()

    list_display = (
        'name',
        'abbr', 
        'slogan', 
        'zone', 
    )

    list_filter = (
        'zone',
    )

admin.site.register(State, StateAdmin)

class TownAdmin(admin.ModelAdmin):
    search_fields = ['name', 'state', 'postal_code']
    ordering = ('name', )
    filter_horizontal = ()

    list_display = (
        'name',
        'abbr',
        'state',
        'postal_code',
    )

    list_filter = (
        'state',
    )

admin.site.register(Town, TownAdmin)