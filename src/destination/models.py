from django.db import models
from .manager import DestinationLinkManager

from rest_framework.reverse import reverse as api_reverse
from django.utils.translation import gettext_lazy as _
from locations.models import Town
from events.models import TransportEvent
from django.db.models.signals import pre_save

class DestinationLink(models.Model):
    event = models.ForeignKey(TransportEvent, verbose_name=_("Event"), on_delete=models.CASCADE, related_name='eventdestination')
    destination = models.ForeignKey("Destination", verbose_name=_("Destination"), on_delete=models.CASCADE)
    total_seats = models.PositiveIntegerField(_("Total Number Of Seats"), default=0)
    used_seats  = models.PositiveIntegerField(_("Number Used Of Seats"), default=0)
    available_seats  = models.PositiveIntegerField(_("Number Of Available Seats"), default=0)
    active = models.BooleanField(_("Active"), default=True)

    objects = DestinationLinkManager()

    def __str__(self):
        return str(self.destination)

    def get_api_uri(self, request=None, place=None):
        return api_reverse(place, kwargs={'id': self.id}, request=request)    

    class Meta:
        db_table = 'transport_destination_links'
        managed = True
        verbose_name = 'Destination Link'
        verbose_name_plural = 'Destination Links'



class Destination(models.Model):
    
    area = models.TextField(_("Destination Area"))
    town = models.ForeignKey(Town, verbose_name=_("Town"), on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.town, self.area)

    def get_api_uri(self, request=None, place=None):
        return api_reverse(place, kwargs={'id': self.id}, request=request)

    class Meta:
        unique_together = ['area', 'town']
        db_table = 'transport_destinations'
        managed = True
        verbose_name = 'Destination'
        verbose_name_plural = 'Destinations'