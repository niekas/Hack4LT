import re
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core import validators
from django.core.mail import send_mail
from django.db import models
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Hacker(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=30, unique=True,
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'), 'invalid')
        ])
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)

    email = models.EmailField(_('Email address'), max_length=254, unique=True)
    email_verified = models.BooleanField(_('Was email approved'), default=False)

    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    repository = models.URLField(_('Your github.com or bitbucket.org account page'), blank=True)
    stackoverflow_user = models.URLField(_('Your Stackoverflow.com account page'), blank=True)
    website = models.URLField(_('Your blog or website'), blank=True)
    description = models.TextField(_('Additional information'), blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def activate(self, domain='demo.damis.lt'):
        if not self.is_active:
            self.is_active = True
            self.save()
            receiver = self.email
            subject = _('{0} account activated').format(domain)
            body = render_to_string('accounts/mail/account_activated.html', {
                'domain': domain,
                'username': self.username,
            })
            sender = settings.DEFAULT_FROM_EMAIL
            send_mail(subject, body, sender, [receiver])
            return True
        return False


class Task1(models.Model):
    user = models.ForeignKey('Hacker')
    file = models.FileField(_('sys_info file'), upload_to='task1')

class Task2(models.Model):
    user = models.ForeignKey('Hacker')
    repository = models.URLField(_('Repository page with task source code'), blank=True)
    description = models.TextField(_('Task description'))
