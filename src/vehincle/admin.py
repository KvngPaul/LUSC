from django.contrib import admin

# Register your models here.
from .models import (
    VehincleMake,
    Vehincle,
    VehincleAssigned
)

class VehincleMakeAdmin(admin.ModelAdmin):
    search_fields = ['make']
    ordering = ('make',)
    filter_horizontal = ()

    list_display = (
        'make',
    )

admin.site.register(VehincleMake, VehincleMakeAdmin)

class VehincleAdmin(admin.ModelAdmin):
    search_fields = ['make', 'model', 'plates', 'color', 'driver', 'destination']

    list_display = (
        'make',
        'model',
        'plates',
        'color',
        'seat',
        'driver',
        'destination',
        'timestamp',
        'active',
    )

    list_filter = (
        'make',
        'model',
        'color',
        'active',
    )

admin.site.register(Vehincle, VehincleAdmin)

admin.site.register(VehincleAssigned)