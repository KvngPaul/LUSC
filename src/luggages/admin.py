from django.contrib import admin

# Register your models here.
from .models import (
    Luggage,
    LuggageBooking,
)

admin.site.register(Luggage)
admin.site.register(LuggageBooking)