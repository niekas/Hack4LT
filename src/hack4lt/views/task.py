from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .account import LoginRequiredMixin, AdminRequiredMixin

from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from hack4lt.models import TaskInfo

from hack4lt.forms import (
    Task1Form,
    Task2Form,
    TaskInfoForm,
)




class UserMixin(object):
    def get_form_kwargs(self):
        return {'user': self.request.user}


class TaskInfoCreate(UserMixin, AdminRequiredMixin, CreateView):
    model = TaskInfo
    form_class = TaskInfoForm
    template_name = 'hack4lt/form.html'

class TaskInfoUpdate(UserMixin, AdminRequiredMixin, UpdateView):
    model = TaskInfo
    form_class = TaskInfoForm
    template_name = 'hack4lt/form.html'

class TaskInfoDelete(AdminRequiredMixin, DeleteView):
    model = TaskInfo
    success_url = reverse_lazy('tasks')


def tasks_view(request):
    return render(request, 'hack4lt/tasks.html', {})

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
