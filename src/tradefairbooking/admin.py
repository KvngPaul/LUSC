from django.contrib import admin

from .models import (
    ExtraMaster,
    TradeFairBooking,
    Tent,
    TentRegister,
)

admin.site.register(ExtraMaster)
admin.site.register(TradeFairBooking)
admin.site.register(Tent)
admin.site.register(TentRegister)