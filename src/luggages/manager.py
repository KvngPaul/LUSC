from django.db import models


class LuggageManager(models.Manager):
    def search(self, booking_id):
        return self.get_queryset().filter(booking=booking_id)


class LuggageBookingQuerySet(models.QuerySet):
    def active(self, user):
        return self.filter(active=True, user=user)


class LuggageBookingManager(models.Manager):
    def get_queryset(self):
        queryset = LuggageBookingQuerySet(self.model, using=self._db)
        return queryset

    def active(self, user):
        return self.get_queryset().active(user)

    def search(self, user):
        return self.get_queryset().active().filter(user=user)
