from django import forms

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()


class UserAdminCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('reg_no', )

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("passwords don't match")
        return confirm_password

    def save(self, commit=False):
        user = super(UserAdminCreationForm, self).save(commit=commit)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            'reg_no',
            'password',
            'active',
            'admin'
        )

    def clean_password(self):
        return self.inintial['password']
