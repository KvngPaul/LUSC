from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from .models import (
    TradeFairBooking,
    ExtraMaster,
    TentRegister,
)
from events.models import TradeFairEvent


@reciever(pre_save, sender=TradeFairBooking)
def booking_pre_save(sender, instance, **kwargs):
    total = 0
    for extra in instance.extras.all():
        total += extra.tot_price
    total += instance.tent.price
    if instance.total != total:
        instance.total = total


@receiver(post_save, sender=TradeFairBooking)
def trade_update(sender, instance, **kwargs):
    instance.tent.used_slots += 1
    instance.tent.save()

    for goods in instance.goods.all():
        goods.used_slots += 1
        goods.save()


@receiver(post_delete, sender=TradeFairBooking)
def trade_downgrade(sender, instance, **kwargs):
    instance.tent.used_slots -= 1
    instance.tent.save()

    for goods in instance.goods.all():
        goods.used_slots -= 1
        goods.save()


@receiver(pre_save, sender=TentRegister, weak=False)
def tent_active(sender, instance, **kwargs):
    if not instance.event:
        instance.event = TradeFairEvent.objects.active().latest()

    used = 0

    for tent in instance.tent_booking.all():
        used += 1
    if instance.used_slots != used:
        instance.used_slots = used
    instance.available_slots = instance.slots - instance.used_slots

    if instance.available_slots == 0 | instance.event.active == False:
        instance.active = False

    elif instance.available_slots > 0 and instance.event.active == True:
        instance.active = True


@receiver(pre_save, sender=ExtraMaster)
def extra_total(sender, instance, **kwargs):
    instance.tot_price = instance.extra.price * instance.unit
    instance.extra.used_slots += instance.unit
    instance.extra.save()


@receiver(post_delete, sender=ExtraMaster)
def extra_unit_delete(sender, instance, **kwargs):
    instance.extra.used_slots -= instance.unit
    instance.extra.save()


@receiver(post_save, sender=TradeFairEvent)
def booking_active(sender, instance, **kwargs):
    if instance.active == False:
        for booking in instance.event_booking.all():
            if booking.active:
                booking.active = False
                booking.save()

        for tent in instance.event_tent.all():
            if tent.active:
                tent.active = False
                tent.save()

    else:
        for booking in instance.event_booking.all():
            if not booking.active:
                booking.active = True
                booking.save()

        for tent in instance.event_tent.all():
            if not tent.active:
                tent.active = True
                tent.save()
