from django.db import models
from rest_framework.reverse import reverse as api_reverse
from django.utils.translation import gettext_lazy as _

class Driver(models.Model):
    first_name      = models.CharField(_("First Name"), max_length=50)
    last_name       = models.CharField(_("Last Name"), max_length=50)
    phone_number    = models.PositiveIntegerField(_("Phone Number"))
    timestamp       = models.DateTimeField(_("Timestamp"), auto_now=False, auto_now_add=True)

    @property
    def fullName(self):
        return self.first_name + ' ' + self.last_name
    
    def __str__(self):
        return self.fullName

    def get_api_uri(self, request=None):
        return api_reverse('api:driver-api:driver-rud', kwargs={'id': self.id}, request=request)    

    class Meta:
        db_table = 'transport_driver'
        managed = True
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'
