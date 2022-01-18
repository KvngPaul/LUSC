from django.db import models

from django.utils.translation import gettext_lazy as _
from driver.models import Driver
from destination.models import (
    Destination,
    DestinationLink,
)
from django.contrib.auth import get_user_model

User = get_user_model()

class Color(models.IntegerChoices):
    BLACK     = 1, _('Black')
    WHITE     = 2, _('White')
    ASH       = 3, _('Ash')
    SILVER    = 4, _('Silver')
    BROWN     = 5, _('Brown')
    BLUE      = 6, _('Blue')
    GREEN     = 7, _('Green')
    MAROON    = 8, _('Maroon')
    RED       = 9, _('Red')

class VehincleMake(models.Model):
    make = models.CharField(_("Make"), max_length=50)
    
    def __str__(self):
        return self.make

    class Meta:
        ordering = ['make']
        db_table = 'transport_vehincle_makes'
        managed = True
        verbose_name = 'Vehincle Make'
        verbose_name_plural = 'Vehincle Makes'


class Vehincle(models.Model):
    make = models.ForeignKey(VehincleMake, verbose_name=_("Make"), on_delete=models.CASCADE)
    model = models.CharField(_("Model"), max_length=50)
    plates = models.CharField(_("Plate Number"), max_length=50)
    color = models.PositiveIntegerField(_("Color"), choices=Color.choices)
    seat = models.PositiveIntegerField(_("Seat"))
    driver = models.OneToOneField(Driver, verbose_name=_("Driver"), on_delete=models.SET_NULL, null=True)
    destination = models.ForeignKey(DestinationLink, verbose_name=_("Destination"), on_delete=models.CASCADE, related_name='vehincledestination')
    active = models.BooleanField(_("Active"), default=True)
    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)
    
    def __str__(self):
        return '{}, {}, {}'.format(self.make, self.model, self.destination)

    class Meta:
        ordering = ['model']
        db_table = 'transport_vehince'
        managed = True
        verbose_name = 'Vehincle'
        verbose_name_plural = 'Vehincles'


class VehincleAssigned(models.Model):
    vehincle = models.ForeignKey(Vehincle, verbose_name=_("Vehincle"), on_delete=models.CASCADE)
    passangers = models.ManyToManyField(User, verbose_name=_("Passangers"))

    def __str__(self):
        return self.vehincle

    class Meta:
        db_table = 'transport_vehincle_assigned'
        managed = True
        verbose_name = 'Vehincle Assigned'
        verbose_name_plural = 'Vehincle Assigned'