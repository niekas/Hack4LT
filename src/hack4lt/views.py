from django.contrib.auth import login, logout, authenticate
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

from hack4lt.forms import LoginForm, RegistrationForm


def index_view(request):
    return render(request, 'hack4lt/home.html', {})


def python_view(reuqest):
    return HttpResponse(_('Not implemented yet.'))


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

def profile_view(request):
    return HttpResponse('Not implemented')
