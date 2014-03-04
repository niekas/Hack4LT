from django.contrib.auth import login, logout, authenticate
from django.core.urlresolvers import reverse_lazy
from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, DetailView

from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.http import int_to_base36, base36_to_int
from django.contrib.auth.tokens import default_token_generator
from django.utils.translation import ugettext_lazy as _
from django.conf import settings



from hack4lt.forms import (
    EmailForm,
    LoginForm,
    PasswordRecoveryForm,
    ProfileForm,
    RegistrationForm,
)
from hack4lt.models import (
    TaskResult,
    Hacker,
)


def login_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            if user is not None and user.is_active:
                next_page = request.POST.get('next') or reverse_lazy('home')
                login(request, user)
                return HttpResponseRedirect(next_page)
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {
            'form': form,
            'request': request,
        })


def logout_view(request):
    logout(request)
    request.session.clear()
    return HttpResponseRedirect('/login/')


def register_view(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse_lazy('home'))
    return render(request, 'accounts/register.html', {
        'form': form,
    })

@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('profile'))
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'hack4lt/task.html', {
        'form': form,
    })




class LoginRequiredMixin(object):
    @method_decorator(login_required(login_url=reverse_lazy('login')))
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class AdminRequiredMixin(object):
    @method_decorator(login_required(login_url=reverse_lazy('login')))
    def dispatch(self, *args, **kwargs):
        user = self.request.user
        if not user.is_superuser:
            return HttpResponseRedirect(reverse_lazy('login'))
        return super(AdminRequiredMixin, self).dispatch(*args, **kwargs)


class ProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = 'hack4lt/profile_detail.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        tasks_done = TaskResult.objects.filter(user=user, done=True)
        context['tasks_done'] = tasks_done
        context['total_points'] = tasks_done.aggregate(points=Sum('total_points'))['points'] or 0
        return context

    def get_object(self, queryset=None):
        return self.request.user



def verify_email_view(request, uidb36, token):
    user = Hacker.objects.get(pk=base36_to_int(uidb36))
    if default_token_generator.check_token(user, token):
        user.email_verified = True
        user.save()
        return HttpResponseRedirect(reverse_lazy('profile'))
    raise Http404


def profile_verify_email_view(request):
    user = request.user
    receiver = user.email
    subject = _('Hack4LT verify email')
    body = render_to_string('accounts/mail/verify_email.html', {
                'username': user.username,
                'url': reverse_lazy('verify-email', kwargs={
                        'uidb36': int_to_base36(user.pk),
                        'token': default_token_generator.make_token(user)
                    }),
            })
    sender = settings.DEFAULT_FROM_EMAIL
    send_mail(subject, body, sender, [receiver])

    return HttpResponse('verify email: ' + user.email)


def reset_password_email_view(request):
    email_form = EmailForm()
    if request.method == 'POST':
        email_form = EmailForm(request.POST)
        if email_form.is_valid():
            receiver = email_form.cleaned_data.get('email')
            user = Hacker.objects.get(email=receiver)
            subject = _('Hack4LT password reset')
            body = render_to_string('accounts/mail/reset_password.html', {
                'username': user.username,
                'url': reverse_lazy('reset-password', kwargs={
                        'uidb36': int_to_base36(user.pk),
                        'token': default_token_generator.make_token(user)
                    }),
            })
            sender = settings.DEFAULT_FROM_EMAIL
            send_mail(subject, body, sender, [receiver])
            return HttpResponse(_('Recovery email sent to: ') + receiver)
    else:
        email_form = EmailForm()
    return render(request, 'accounts/reset_password.html', {
                'form': email_form,
            })

def reset_password_view(request, uidb36, token):
    user = Hacker.objects.get(pk=base36_to_int(uidb36))
    if default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = PasswordRecoveryForm(request.POST)
            if form.is_valid():
                user = form.save(uidb36, token)
                password = form.cleaned_data.get('password')
                user = authenticate(username=user.username, password=password)
                if user is not None and user.is_active:
                    login(request, user)
                return HttpResponseRedirect(reverse_lazy('home'))
        else:
            form = PasswordRecoveryForm()
        return render(request, 'accounts/set_password.html', {
                'form': form,
            })
    raise Http404
