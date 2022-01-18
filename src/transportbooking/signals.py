from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from events.models import TransportEvent


@receiver(post_save, sender=TransportEvent)
def school_active(sender, instance, created, **kwargs):
    if not created:
        if instance.schoolbooking != None and instance.active == False:
            for booking in instance.schoolbooking.all():
                if booking.active == True:
                    booking.active = False
                    booking.save()


@receiver(post_save, sender=TransportEvent)
def private_active(sender, instance, created, **kwargs):
    if not created:
        if instance.privatebooking != None and instance.active == False:
            for booking in instance.privatebooking.all():
                if booking.active == True:
                    booking.active = False
                    booking.save()



@receiver(post_save, sender=TransportEvent)
def organized_active(sender, instance, created, **kwargs):
    if not created:
        if instance.organizedbooking != None and instance.active == False:
            for booking in instance.organizedbooking.all():
                if booking.active == True:
                    booking.active = False
                    booking.save()


