from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from events.models import TradeFairEvent
from tradefair.models import (
    GoodsRegister,
    ExtraRegister,
)
from .manager import TentRegisterManager, TradeFairBookingManager

User = get_user_model()


class Tent(models.Model):
    name = models.CharField(_("Tent"), max_length=50)
    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tradefair_tent'
        managed = True
        verbose_name = 'Tent'
        verbose_name_plural = 'Tents'


class TentRegister(models.Model):
    event = models.ForeignKey(TradeFairEvent, verbose_name=_(
        "Event"), on_delete=models.CASCADE, related_name='event_tent')
    tent = models.ForeignKey(Tent, verbose_name=_(
        "Tent"), on_delete=models.CASCADE, related_name='tent_register')
    price = models.DecimalField(_("Price"), max_digits=8, decimal_places=2)
    note = models.TextField(_("Tent Note"))

    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)
    slots = models.PositiveIntegerField(_("Slots"))
    used_slots = models.PositiveIntegerField(_("Used Slots"), default=0)
    available_slots = models.PositiveIntegerField(
        _("Available Slots"), default=0)

    active = models.BooleanField(_("Active"), default=True)

    objects = TentRegisterManager()

    def __str__(self):
        return '{}, {}'.format(self.event, self.tent)

    class Meta:
        db_table = 'tradefair_tent_register'
        managed = True
        verbose_name = 'Tent Register'
        verbose_name_plural = 'Tent Registers'


class ExtraMaster(models.Model):
    booking = models.ForeignKey("TradeFairBooking", verbose_name=_(
        "Booking"), on_delete=models.CASCADE, related_name='booking_set')
    extra = models.ForeignKey(ExtraRegister, verbose_name=_(
        "Extra"), on_delete=models.CASCADE, related_name='extra_set')
    unit = models.PositiveSmallIntegerField(_("Unit"))
    tot_price = models.DecimalField(
        _("Total Price"), max_digits=8, decimal_places=2)
    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)

    def __str__(self):
        return '{}, {}'.format(self.booking, self.extra)

    class Meta:
        db_table = 'tradefair_extra_master'
        managed = True
        verbose_name = 'Extra Master'
        verbose_name_plural = 'Extra Masters'


class TradeFairBooking(models.Model):
    event = models.ForeignKey(TradeFairEvent, verbose_name=_(
        "Event"), on_delete=models.CASCADE, related_name='event_booking')
    user = models.ForeignKey(User, verbose_name=_(
        "User"), on_delete=models.CASCADE, related_name='user_booking')
    tent = models.ForeignKey(TentRegister, verbose_name=_(
        "Tent"), on_delete=models.SET_NULL, null=True, related_name='tent_booking')
    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)
    goods = models.ManyToManyField(GoodsRegister, verbose_name=_(
        "Goods"), related_name='goods_booking')
    extras = models.ManyToManyField(ExtraRegister, verbose_name=_(
        "Extras"), through='ExtraMaster', related_name='extra_booking')
    total = models.DecimalField(
        _("Total Price"), max_digits=8, decimal_places=2, null=True, blank=True)

    active = models.BooleanField(_("Active"), default=True)
    approved = models.BooleanField(_("Approved"), default=False)

    objects = TradeFairBookingManager()

    def __str__(self):
        return '{}, {}'.format(self.user, self.event)

    def save(self, *args, **kwargs):
        total = 0
        for extra in self.extras.all():
            total += extra.tot_price
        total += self.tent.price
        if self.total != total:
            self.total = total
        super(TradeFairBooking, self).save(*args, **kwargs)

    class Meta:
        db_table = 'tradefair_bookings'
        managed = True
        verbose_name = 'Trade Fair Booking'
        verbose_name_plural = 'Trade Fair Bookings'
