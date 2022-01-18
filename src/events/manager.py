from django.db import models


class SessionQuerySet(models.QuerySet):
    def get_latest(self):
        return self.latest('timestamp')


class SessionManager(models.Manager):
    def get_queryset(self):
        queryset = SessionQuerySet(self.model, using=self._db)
        return queryset

    def create_new(self):
        latest = self.get_queryset().get_latest()
        year_1 = latest.year_2
        year_2 = year_1 + 1
        new = self.get_queryset().create(year_1=year_1, year_2=year_2)
        return new


# Transport Event
class TransportQuerySet(models.QuerySet):
    def active(self):
        return self.filter(active=True)


class TransportManager(models.Manager):
    def get_queryset(self):
        queryset = TransportQuerySet(self.model, using=self._db)
        return queryset

    def active(self):
        return self.get_queryset().active()

    def deactivate(self, id=None):
        if id is None:
            qs = self.active()
            if qs.exists():
                for query in qs:
                    query.active = False
                    query.save()
            return None

        else:
            qs = self.get(id=id)
            qs.active = False
            qs.save()
            return qs

    def deactivate_others(self, id=None):
        if id is None:
            return None

        else:
            qs = self.all().exclude(id=id)
            for query in qs:
                if query.active:
                    query.active = False
                    query.save()
            return qs


# Luggage Event
class LuggageQuerySet(models.QuerySet):
    def active(self):
        return self.filter(active=True)

    def deposite_active(self):
        return self.filter(deposit_active=True)


class LuggageManager(models.Manager):
    def get_queryset(self):
        queryset = LuggageQuerySet(self.model, using=self._db)
        return queryset

    def active(self):
        return self.get_queryset().active()

    def deposit_active(self):
        return self.get_queryset().deposit_active()

    def deactivate(self, id=None):
        if id is None:
            qs = self.active()
            if qs.exists():
                for query in qs:
                    query.active = False
                    query.save()
            return None

        else:
            qs = self.get(id=id)
            qs.active = False
            qs.save()
            return qs

    def deactivate_others(self, id=None):
        if id is None:
            return None

        else:
            qs = self.all().exclude(id=id)
            for query in qs:
                if query.active:
                    query.active = False
                    query.save()
            return qs


# Trade Fair Event
class TradeFairQueryset(models.QuerySet):
    def active(self):
        return self.filter(active=True)

    def deposite_active(self):
        return self.filter(deposit_active=True)


class TradeFairManager(models.Manager):
    def get_queryset(self):
        queryset = TradeFairQueryset(self.model, using=self._db)
        return queryset

    def active(self):
        return self.get_queryset().active()

    def deposit_active(self):
        return self.get_queryset().deposit_active()

    def deactivate(self, id=None):
        if id is None:
            qs = self.active()
            if qs.exists():
                for query in qs:
                    query.active = False
                    query.save()
            return None

        else:
            qs = self.get(id=id)
            qs.active = False
            qs.save()
            return qs

    def deactivate_others(self, id=None):
        if id is None:
            return None

        else:
            qs = self.all().exclude(id=id)
            for query in qs:
                if query.active:
                    query.active = False
                    query.save()
            return qs
