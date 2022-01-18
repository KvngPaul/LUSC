from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from .models import(
    ExtraRegister,
    GoodsRegister,
)

from events.models import TradeFairEvent


@receiver(post_save, sender=TradeFairEvent)
def goods_active(sender, instance, **kwargs):
    if instance.active == False:
        for goods in instance.event_goods.all():
            if goods.active:
                goods.active = False
                goods.save()
    else:
        for goods in instance.event_goods.all():
            if not goods.active:
                goods.active = True
                goods.save()


@receiver(pre_save, sender=GoodsRegister, weak=False)
def goods_active(sender, instance, **kwargs):
    if not instance.event:
        instance.event = TradeFairEvent.objects.active().latest()

    used = 0

    for goods in instance.goods_booking.all():
        used += 1
    if instance.used_slots != used:
        instance.used_slots = used
    instance.available_slots = instance.slots - instance.used_slots

    if instance.available_slots == 0 | instance.event.active == False:
        instance.active = False

    elif instance.available_slots > 0 and instance.event.active == True:
        instance.active = True


@receiver(post_save, sender=TradeFairEvent)
def extra_active(sender, instance, **kwargs):
    if instance.active == False:
        for extra in instance.event_extra.all():
            if extra.active:
                extra.active = False
                extra.save()
    else:
        for extra in instance.event_extra.all():
            if not extra.active:
                extra.active = True
                extra.save()


@receiver(pre_save, sender=ExtraRegister, weak=False)
def extra_active(sender, instance, **kwargs):
    if not instance.event:
        instance.event = TradeFairEvent.objects.active().latest()

    used = 0

    for extra in instance.extra_set.all():
        used += extra.unit
    if instance.used_slots != used:
        instance.used_slots = used
    instance.available_slots = instance.slots - instance.used_slots

    if instance.available_slots == 0 | instance.event.active == False:
        instance.active = False

    elif instance.available_slots > 0 and instance.event.active == True:
        instance.active = True
