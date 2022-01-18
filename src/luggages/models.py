from django.db import models
from django.utils.translation import gettext_lazy as _
from events.models import LuggageEvent
from .manager import LuggageBookingManager, LuggageManager
from django.contrib.auth import get_user_model

User = get_user_model()


class LuggageType(models.IntegerChoices):
    BOX = 1, _('Box')
    BAG = 2, _('Bags')
    SACK = 3, _('Sacks/Ghana Must Go')
    BUCKET = 4, _('Bucket')


class LugagageSize(models.IntegerChoices):
    SMALL = 1, _('S')
    MEDIUM = 2, _('M')
    LARGE = 3, _('L')
    EXTRA_LARGE = 4, _('XL')


class Luggage(models.Model):
    # booking have to be set in the view
    booking = models.ForeignKey("LuggageBooking", verbose_name=_(
        "Luggage Booking"), related_name='luggage_booking', on_delete=models.CASCADE, blank=True)

    l_type = models.PositiveIntegerField(
        _("Luggage Type"), choices=LuggageType.choices)
    size = models.PositiveIntegerField(
        _("Luggage Size"), choices=LugagageSize.choices)
    primary_color = models.CharField(_("Luggage Color"), max_length=15)
    secondary_color = models.CharField(
        _("Luggage Color"), max_length=15, blank=True, null=True)

    deposited = models.BooleanField(_("Deposited"), default=False)
    date_deposited = models.DateTimeField(
        _("Date Deposited"), null=True, blank=True)

    collected = models.BooleanField(_("Collected"), default=False)
    date_collected = models.DateTimeField(
        _("Date Collected"), null=True, blank=True)

    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)

    objects = LuggageManager()

    def __str__(self):
        return '{}-{}-{}'.format(self.booking, self.l_type, self.size, self.primary_color, self.secondary_color)

    class Meta:
        db_table = 'luggage'
        managed = True
        verbose_name = 'Luggage'
        verbose_name_plural = 'Luggages'


class LuggageBooking(models.Model):
    event = models.ForeignKey(LuggageEvent, verbose_name=_(
        "Event"), on_delete=models.CASCADE, related_name='luggage_event', blank=True)
    user = models.ForeignKey(User, verbose_name=_(
        "User"), on_delete=models.CASCADE, blank=True)
    active = models.BooleanField(_("Active"), default=True)

    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)

    objects = LuggageBookingManager()

    def __str__(self):
        return '{}, {}'.format(self.user, self.event)

    class Meta:
        db_table = 'luggage_bookings'
        managed = True
        verbose_name = 'Luggage Booking'
        verbose_name_plural = 'Luggage Bookings'
