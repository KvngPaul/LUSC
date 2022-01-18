from django.db.models.signals import post_save, pre_save
from events.models import LuggageEvent
from .models import LuggageBooking, Luggage
from django.dispatch import receiver

from django.utils import timezone


@receiver(post_save, sender=LuggageEvent)
def luggage_booking_active(sender, instance, created, **kwargs):
    if not created:
        if instance.active == False:
            for booking in instance.luggage_event.all():
                if booking.active:
                    booking.active = False
                    booking.save()
        else:
            for booking in instance.luggage_event.all():
                if booking.active == False:
                    booking.active = True
                    booking.save()


@receiver(pre_save, sender=LuggageBooking)
def luggage_booking_active(sender, instance, **kwargs):
    event = LuggageEvent.objects.active().latest()
    instance.event = event


@receiver(pre_save, sender=Luggage)
def luggage_dep_coll(sender, instance, **kwargs):
    if instance.deposited and not instance.date_deposited:
        instance.date_deposited = timezone.now()

    if instance.collected and not instance.date_collected:
        instance.date_collected = timezone.now()
