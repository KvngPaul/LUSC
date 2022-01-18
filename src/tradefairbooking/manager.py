from django.db import models


class TentRegisterQuerySet(models.QuerySet):
    def active(self):
        return self.filter(active=True)


class TentRegisterManager(models.Manager):
    def get_queryset(self):
        queryset = TentRegisterQuerySet(self.model, using=self._db)
        return queryset

    def active(self):
        return self.get_queryset().active()


class TradeFairBookingQuerySet(models.QuerySet):
    def active(self):
        return self.filter(active=True)


class TradeFairBookingManager(models.Manager):
    def get_queryset(self):
        queryset = TradeFairBookingQuerySet(self.model, using=self._db)
        return queryset

    def active(self):
        return self.get_queryset().active()
