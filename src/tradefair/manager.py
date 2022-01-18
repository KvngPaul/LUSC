from django.db import models


class GoodsRegisterQuerySet(models.QuerySet):
    def active(self):
        return self.filter(active=True)


class GoodsRegisterManager(models.Manager):
    def get_queryset(self):
        queryset = GoodsRegisterQuerySet(self.model, using=self._db)
        return queryset

    def active(self):
        return self.get_queryset().active()


class ExtraRegisterQuerySet(models.QuerySet):
    def active(self):
        return self.filter(active=True)


class ExtraRegisterManager(models.Manager):
    def get_queryset(self):
        queryset = ExtraRegisterQuerySet(self.model, using=self._db)
        return queryset

    def active(self):
        return self.get_queryset().active()
