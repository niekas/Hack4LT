from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from hack4lt.forms import (
    Task1Form,
    Task2Form,
    TaskInfoForm,
)
from hack4lt.models import TaskInfo, TaskResultMixin
from hack4lt.views.account import AdminRequiredMixin


class UserMixin(object):
    def form_valid(self, form):
        response = super(UserMixin, self).form_valid(form)
        form.instance.user = self.request.user
        form.instance.save()
        return response

class TaskInfoCreate(UserMixin, AdminRequiredMixin, CreateView):
    model = TaskInfo
    form_class = TaskInfoForm
    template_name = 'hack4lt/form.html'
    success_url = reverse_lazy('tasks')

class TaskInfoUpdate(UserMixin, AdminRequiredMixin, UpdateView):
    model = TaskInfo
    form_class = TaskInfoForm
    template_name = 'hack4lt/form.html'
    success_url = reverse_lazy('tasks')

class TaskInfoList(AdminRequiredMixin, ListView):
    model = TaskInfo
    paginate_by = 30
    template_name = 'hack4lt/task_list.html'
    success_url = reverse_lazy('tasks')

    def get_context_data(self, **kwargs):
        context = super(TaskInfoList, self).get_context_data(**kwargs)
        user_tasks = TaskResultMixin.objects.filter(user=self.request.user)
        context['tasks_done'] = dict(user_tasks.filter(done=True).
                                            values_list('pk', 'total_points'))
        return context


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
