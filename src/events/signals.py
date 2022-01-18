from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
import datetime

from .models import TransportEvent, LuggageEvent, TradeFairEvent
from django.utils import timezone


# Transport
@receiver(post_save, sender=TransportEvent)
def transport_event_active(sender, instance, created, **kwargs):
    if created:
        TransportEvent.objects.deactivate_others(id=instance.id)


# Luggage
@receiver(post_save, sender=LuggageEvent)
def luggage_event_active(sender, instance, created, **kwargs):
    if created:
        LuggageEvent.objects.deactivate_others(id=instance.id)


# Luggage
@receiver(post_save, sender=TradeFairEvent)
def luggage_event_active(sender, instance, created, **kwargs):
    if created:
        TradeFairEvent.objects.deactivate_others(id=instance.id)
