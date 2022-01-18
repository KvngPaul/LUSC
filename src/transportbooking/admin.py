from django.contrib import admin

from .models import (
    SchoolTransportBooking,
    PrivateTransportBooking,
    OrganizedTransportBooking,
)

admin.site.register(SchoolTransportBooking)
admin.site.register(PrivateTransportBooking)
admin.site.register(OrganizedTransportBooking)