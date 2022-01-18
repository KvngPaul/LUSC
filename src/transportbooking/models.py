from django.db import models

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from destination.models import DestinationLink
from locations.models import Town
from vehincle.models import VehincleMake
from events.models import TransportEvent

User = get_user_model()

class SchoolTransportBooking(models.Model):
    event = models.ForeignKey(TransportEvent, verbose_name=_("Event"), on_delete=models.SET_NULL, null=True, related_name='schoolbooking')
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    destination = models.ForeignKey(DestinationLink, verbose_name=_("Destination"), on_delete=models.CASCADE, related_name='bookingdestination')
    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)

    active = models.BooleanField(_("Active"), default=True)
    approved = models.BooleanField(_("Approved"), default=False)
    
    def __str__(self):
        return '{} {}'.format(self.user, self.destination)

    class Meta:
        db_table = 'transport_booking_school'
        managed = True
        verbose_name = 'School Transport Booking'
        verbose_name_plural = 'School Transport Bookings'




class PrivateTransportBooking(models.Model):
    event = models.ForeignKey(TransportEvent, verbose_name=_("Event"), on_delete=models.SET_NULL, null=True, related_name='privatebooking')
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE, related_name='private_user')
    town = models.ForeignKey(Town, verbose_name=_("Town"), on_delete=models.CASCADE)
    other_users = models.ManyToManyField(User, verbose_name=_("Other Students"), related_name='other_users')

    vehincle_make = models.ForeignKey(VehincleMake, verbose_name=_("Vehincle Make"), on_delete=models.CASCADE)
    vehincle_model = models.CharField(_("Vehincle Model"), max_length=50)
    vehincle_color = models.CharField(_("Vehincle Color"), max_length=9)

    driver_name = models.CharField(_("Driver Name"), max_length=50)
    driver_phone_number = models.IntegerField(_("Driver Phone Number"))

    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)
    active = models.BooleanField(_("Active"), default=True)
    approved = models.BooleanField(_("Approved"), default=False)

    
    def __str__(self):
        return str(self.user)

    class Meta:
        db_table = 'transport_booking_private'
        managed = True
        verbose_name = 'Private Transport Booking'
        verbose_name_plural = 'Private Transport Bookings'





class OrganizedTransportBooking(models.Model):
    event = models.ForeignKey(TransportEvent, verbose_name=_("Event"), on_delete=models.SET_NULL, null=True, related_name='organizedbooking')
    organizer = models.ForeignKey(User, verbose_name=_("Organizer"), on_delete=models.CASCADE, related_name='organizer')
    town = models.ForeignKey(Town, verbose_name=_("Town"), on_delete=models.CASCADE)
    users = models.ManyToManyField(User, verbose_name=_("Students"))

    vehincle_make = models.ForeignKey(VehincleMake, verbose_name=_("Vehincle Make"), on_delete=models.CASCADE)
    vehincle_model = models.CharField(_("Vehincle Model"), max_length=50)
    vehincle_color = models.CharField(_("Vehincle Color"), max_length=9)

    driver_name = models.CharField(_("Driver Name"), max_length=50)
    driver_phone_number = models.IntegerField(_("Driver Phone Number"))

    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)
    active = models.BooleanField(_("Active"), default=True)
    approved = models.BooleanField(_("Approved"), default=False)
    
    def __str__(self):
        return str(self.organizer)

    class Meta:
        db_table = 'transport_booking_organized'
        managed = True
        verbose_name = 'Organized Transport Booking'
        verbose_name_plural = 'Organized Transport Bookings'
