from django.db import models
from django.utils.translation import gettext_lazy as _
from .manager import SessionManager, TransportManager, LuggageManager, TradeFairManager
from rest_framework.reverse import reverse as api_reverse


class Session(models.Model):
    year_1 = models.SmallIntegerField(_("Start Year"))
    year_2 = models.SmallIntegerField(_("End Year"))
    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)

    def __str__(self):
        return '{}/{}'.format(self.year_1, self.year_2)

    objects = SessionManager()

    class Meta:
        ordering = ['year_1']
        unique_together = ['year_1', 'year_2']
        db_table = 'events_tranport_sessions'
        managed = True
        verbose_name = 'Session'
        verbose_name_plural = 'Sessions'


class Semester(models.IntegerChoices):
    ALPHA = 1, _('Alpha')
    OMEGA = 2, _('Omega')


class TransportEvent(models.Model):
    session = models.ForeignKey(Session, verbose_name=_(
        "Session"), on_delete=models.CASCADE)
    semester = models.PositiveIntegerField(
        _("Semester"), choices=Semester.choices)
    start_date = models.DateTimeField(_("Registration Start Date"))
    end_date = models.DateTimeField(_("Registration End Date"))
    payment_start_date = models.DateTimeField(_("Payment Start Date"))
    payment_end_date = models.DateTimeField(_("Payment End Date"))
    transport_date = models.DateField(_("Transport Date"))
    active = models.BooleanField(_("Active"), default=True)
    payment_active = models.BooleanField(_("Payment Active"), default=False)
    timestamp = models.DateTimeField(
        _("Timestamp"), auto_now_add=True, null=True)

    objects = TransportManager()

    def __str__(self):
        return '{} - {}'.format(self.session, self.get_semester_display())

    def get_api_uri(self, request=None, place=None):
        return api_reverse(place, kwargs={'id': self.id}, request=request)

    class Meta:
        unique_together = ['session', 'semester',
                           'start_date', 'end_date', 'payment_start_date', 'payment_end_date', 'transport_date']
        db_table = 'events_transport'
        managed = True
        verbose_name = 'Transport Event'
        verbose_name_plural = 'Transport Events'


# Remove the null values on the deposite dates
class LuggageEvent(models.Model):
    session = models.ForeignKey(Session, verbose_name=_(
        "Session"), on_delete=models.CASCADE)
    semester = models.PositiveIntegerField(
        _("Semester"), choices=Semester.choices)
    start_date = models.DateTimeField(_("Registration Start Date"))
    end_date = models.DateTimeField(_("Registraion End Date"))
    deposit_start_date = models.DateTimeField(_("Deposit Start Date"))
    deposit_end_date = models.DateTimeField(_("Deposit End Date"))
    deposit_note = models.TextField(
        _("Note on Deposit procedure"), blank=True, null=True)
    deposit_active = models.BooleanField(_("Deposite Status"), default=False)
    active = models.BooleanField(_("Active"), default=True)
    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)

    objects = LuggageManager()

    def __str__(self):
        return '{} - {}'.format(self.session, self.get_semester_display())

    class Meta:
        unique_together = ['session', 'semester', 'start_date',
                           'end_date', 'deposit_start_date', 'deposit_end_date']
        db_table = 'events_luggage'
        managed = True
        verbose_name = 'Luggage Event'
        verbose_name_plural = 'Luggage Events'


class TradeFairEvent(models.Model):
    session = models.ForeignKey(Session, verbose_name=_(
        "Session"), on_delete=models.CASCADE)
    semester = models.PositiveIntegerField(
        _("Semester"), choices=Semester.choices)
    theme = models.CharField(_("Event Theme"), max_length=50)
    start_date = models.DateTimeField(_("Booking Start Date"))
    end_date = models.DateTimeField(_("Booking End Date"))
    fair_start_date = models.DateTimeField(_("Trade Fair Start Date"))
    fair_end_date = models.DateTimeField(
        _("Trade Fair End Date"))
    fair_note = models.TextField(_("Note on Trade Fair procedure"))
    active = models.BooleanField(_("Active"), default=True)
    timestamp = models.DateTimeField(
        _("Timestamp"), auto_now_add=True)

    objects = TradeFairManager()

    def __str__(self):
        return '{}({} - {})'.format(self.theme, self.session, self.get_semester_display())

    class Meta:
        unique_together = ['session', 'semester', 'theme',
                           'start_date', 'end_date', 'fair_start_date', 'fair_end_date']
        db_table = 'events_trade_fair'
        managed = True
        verbose_name = 'Trade Fair Event'
        verbose_name_plural = 'Trade Fair Events'
