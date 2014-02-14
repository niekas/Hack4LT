from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from hack4lt.forms import (
    Task1Form,
    Task2Form,
)


def index_view(request):
    return HttpResponseRedirect(reverse_lazy('lectures'))

def about_view(request):
    return render(request, 'hack4lt/home.html', {})

def lectures_view(request):
    return render(request, 'hack4lt/lectures.html', {})

def events_view(request):
    return render(request, 'hack4lt/events.html', {})

def tasks_view(request):
    return render(request, 'hack4lt/tasks.html', {})

@login_required(login_url=reverse_lazy('login'))
def admin_view(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse_lazy('login'))
    return render(request, 'hack4lt/admin.html', {})


@login_required(login_url=reverse_lazy('login'))
def task_view(request, task_id):
    if task_id == '1':
        form_class = Task1Form
    elif task_id == '2':
        form_class = Task2Form

    if request.method == 'POST':
        form = form_class(data=request.POST, files=request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('tasks'))
    else:
        form = form_class(user=request.user)
    return render(request, 'hack4lt/task.html', {
            'form': form,
        })
