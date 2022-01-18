from django.db import models

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from events.models import TradeFairEvent
from .manager import GoodsRegisterManager, ExtraRegisterManager


User = get_user_model()


def image_directory(instance, filename):
    instanceClass = instance.__class__
    identifier = instance.name

    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'tradefair/images/{instance_class}/{identifier}/{filename}'.format(instance_class=instanceClass, identifier=identifier, filename=filename)


class Goods(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    goods_image = models.ImageField(
        _("Image"), upload_to=image_directory)
    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tradefair_goods'
        managed = True
        verbose_name = 'Goods'
        verbose_name_plural = 'Goods'


class GoodsRegister(models.Model):
    event = models.ForeignKey(TradeFairEvent, verbose_name=_(
        "Event"), on_delete=models.CASCADE, related_name='event_goods')
    goods = models.ForeignKey(Goods, verbose_name=_(
        "Goods"), on_delete=models.CASCADE, related_name='goods_register')
    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)
    slots = models.PositiveIntegerField(_("Slots"))
    used_slots = models.PositiveIntegerField(_("Used Slots"), default=0)
    available_slots = models.PositiveIntegerField(
        _("Available Slots"), default=0)

    active = models.BooleanField(_("Active"), default=True)

    objects = GoodsRegisterManager()

    def __str__(self):
        return '{}, {}'.format(self.goods, self.event)

    class Meta:
        db_table = 'tradefair_goods_register'
        managed = True
        verbose_name = 'Goods Register'
        verbose_name_plural = 'Goods Registers'


class Extra(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    extra_image = models.ImageField(
        _("Image"), upload_to=image_directory, blank=True, null=True)
    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tradefair_extras'
        managed = True
        verbose_name = 'Extra'
        verbose_name_plural = 'Extras'


class ExtraRegister(models.Model):
    event = models.ForeignKey(TradeFairEvent, verbose_name=_(
        "Event"), on_delete=models.CASCADE, related_name='event_extra')
    extra = models.ForeignKey(Extra, verbose_name=_(
        "Extra"), on_delete=models.CASCADE, related_name='extra_register')
    price = models.DecimalField(_("Price"), max_digits=8, decimal_places=2)

    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)
    slots = models.PositiveIntegerField(_("Slots"))
    used_slots = models.PositiveIntegerField(_("Used Slots"), default=0)
    available_slots = models.PositiveIntegerField(
        _("Available Slots"), default=0)

    active = models.BooleanField(_("Active"), default=True)

    objects = ExtraRegisterManager()

    def __str__(self):
        return '{}, {}'.format(self.extra, self.event)

    class Meta:
        db_table = 'tradefair_extra_register'
        managed = True
        verbose_name = 'Extra Register'
        verbose_name_plural = 'Extra Registers'
