from django.db import models

from django.utils.translation import gettext_lazy as _

class GeoZones(models.IntegerChoices):
    NORTHCENTRAL  = 1, _('North Central')
    NORTHEAST     = 2, _('North East')
    NORTHWEST     = 3, _('North West')
    SOUTHEAST     = 4, _('South East')
    SOUTHWEST     = 5, _('South West')
    SOUTHSOUTH    = 6, _('South South')


class State(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    abbr = models.CharField(_("Abbreviation"), max_length=4)
    slogan = models.CharField(_("Slogan"), max_length=50)
    zone = models.SmallIntegerField(_("GeoPolitical Zone"), choices=GeoZones.choices)
    
    def __str__(self):
        return '{}({})'.format(self.name, self.abbr)

    class Meta:
        db_table = 'location_state'
        managed = True
        verbose_name = 'State'
        verbose_name_plural = 'States'


class Town(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    abbr = models.CharField(_("Abbreviation"), max_length=7)
    state = models.ForeignKey(State, verbose_name=_("State"), on_delete=models.CASCADE)
    postal_code = models.PositiveIntegerField()

    
    def __str__(self):
        return '{}, {}'.format(self.state, self.name)

    class Meta:
        ordering = ['state', 'name']
        db_table = 'location_town'
        managed = True
        verbose_name = 'Town'
        verbose_name_plural = 'Towns'