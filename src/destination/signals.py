from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from events.models import TransportEvent
from vehincle.models import Vehincle
from .models import DestinationLink
from transportbooking.models import SchoolTransportBooking

# Signals For Transport Event
@receiver(post_save, sender=TransportEvent)
def destination_active(sender, instance, created, **kwargs):
    if not created:
        if instance.eventdestination != None and instance.active == False:
            for destination in instance.eventdestination.all():
                if destination.active == True:
                    destination.active = False
                    destination.save()
                for vehincle in destination.vehincledestination.all():
                    if vehincle.active == True:
                        vehincle.active = False
                        vehincle.save()



# Signals For Vehincle
@receiver(post_save, sender=Vehincle)
def destination_seats(sender, instance, created, **kwargs):
        destinations = DestinationLink.objects.all()
        for destination in destinations:
            total = 0
            for vehincle in destination.vehincledestination.all():
                total += vehincle.seat
            destination.total_seats = total
            destination.available_seats = destination.total_seats - destination.used_seats
            destination.save()


@receiver(post_delete, sender=Vehincle)
def destination_seats_delete(sender, instance, **kwargs):
        destinations = DestinationLink.objects.all()
        for destination in destinations:
            total = 0
            for vehincle in destination.vehincledestination.all():
                total += vehincle.seat
            destination.total_seats = total
            destination.available_seats = destination.total_seats - destination.used_seats
            destination.save()



# Signals For Destination
@receiver(pre_save, sender=DestinationLink)
def destination_save(sender, instance, **kwargs):
    if instance.available_seats < 0:
        raise Exception('Number of Booked Seats Exceeds Number of Available Seats')
    
    if instance.event.active == True and instance.available_seats > 0:
        if instance.active == False:
            instance.active = True

    elif instance.available_seats == 0:
        if instance.active == True:
            instance.active = False



# Signals For Bookings
@receiver(post_save, sender=SchoolTransportBooking)
def destination_booking(sender, instance, created, **kwargs):
    destinations = DestinationLink.objects.all()
    for destination in destinations:
        destination.used_seats = destination.bookingdestination.all().count()
        destination.available_seats = destination.total_seats - destination.used_seats
        destination.save()

@receiver(post_delete, sender=SchoolTransportBooking)
def destination_booking_delete(sender, instance, **kwargs):
    destinations = DestinationLink.objects.all()
    for destination in destinations:
        destination.used_seats = destination.bookingdestination.all().count()
        destination.available_seats = destination.total_seats - destination.used_seats
        destination.save()
