from django.db import models

# Create your models here.

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
)

from django.utils.translation import gettext_lazy as _



from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token 



class UserManager(BaseUserManager):
    def create_user(self, reg_no, password=None, is_staff=False, is_admin=False, is_active=True):
        if not reg_no:
            raise ValueError('Users must enter a valid registration number')

        if not password:
            raise ValueError('Passwords are required!')

        user = self.model(
            reg_no = reg_no,
        )
        user.set_password(password)
        user.active = is_active
        user.staff = is_staff
        user.admin = is_admin
        user.save(using=self.db)
        return user

    def create_staffuser(self, reg_no, password=None):
        user = self.create_user(
            reg_no,
            password=password,
            is_staff = True,
        )
        return user

    def create_superuser(self, reg_no, password=None):
        user = self.create_user(
            reg_no,
            password=password,
            is_staff = True,
            is_admin = True,
        )
        return user

    

class User(AbstractBaseUser):
    reg_no = models.IntegerField(_("Registration Number"), unique=True)
    active = models.BooleanField(_("Active"), default=True)
    staff = models.BooleanField(_("Staff"), default=False)
    admin = models.BooleanField(_("Admin"), default=False)

    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)
    confirm = models.BooleanField(_("Confirmed"), default=False)
    confirmed_date = models.DateTimeField(_("Confirmed Date"), blank=True, null=True)

    USERNAME_FIELD = 'reg_no'
    REQUIRED_FIELD = []

    objects = UserManager()

    def __str__(self):
        return str(self.reg_no)

    def has_perm(self, perm, obj=None):
        return True

    def has_perms(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
     if created:
          Token.objects.create(user=instance)
    