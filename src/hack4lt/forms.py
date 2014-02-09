from django import forms
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

from hack4lt.models import Hacker




class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Hacker
        fields = ('username', 'first_name', 'last_name', 'email', 'repository',
                'stackoverflow_user', 'description')


class LoginForm(forms.Form):
    username = forms.CharField(label=_('Username'), max_length=100)
    password = forms.CharField(label=_('Password'), max_length=128,
                        widget=forms.PasswordInput(render_value=False))

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        if self.errors:
            return cleaned_data

        user = authenticate(**cleaned_data)
        if not user:
            raise forms.ValidationError(_('Username or password is incorrect'))
        cleaned_data['user'] = user
        return cleaned_data
