from django.db import models
from django.db.models import Q
from events.models import TransportEvent

class DestinationLinkQuerySet(models.QuerySet):

    def active(self):
        return self.filter(active=True)


class DestinationLinkManager(models.Manager):

    def get_queryset(self):
        queryset = DestinationLinkQuerySet(self.model, using=self._db)
        return queryset

    def active(self):
        return self.get_queryset().active()

    def event(self):
        event = TransportEvent.objects.active().latest('timestamp')
        return self.get_queryset().filter(event=event)