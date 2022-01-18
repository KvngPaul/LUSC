from django.contrib import admin

from django.contrib.auth import get_user_model

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import (
    UserAdminChangeForm,
    UserAdminCreationForm
)

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    search_fields = ['reg_no']
    ordering = ('reg_no', )
    filter_horizontal = ()

    list_display = (
        'reg_no',
        'active',
        'staff',
        'admin'
    )

    list_filter = (
        'admin',
        'staff',
        'active'
    )

    fieldsets = (
        (None, {'fields': ('reg_no', 'password')}),
        ('Personal Info', {'fields': ()}),
        ('Permissions', {'fields': ('admin', 'staff', 'active')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('reg_no', 'password', 'confirm_password')
        }),
    )

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm


admin.site.register(User, UserAdmin)

admin.site.unregister(Group)