from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from hack4lt.forms import (
    CommentForm,
    Task1Form,
    Task2Form,
    TaskAplinkaResultForm,
    TaskInfoForm,
    TaskPythonResultForm,
    TaskResultForm,
    TaskSeminarasResultForm,
)
from hack4lt.models import (
    Topic,
    TaskComment,
    TaskInfo,
    TaskResult,
    TaskAplinkaResult,
    TaskPythonResult,
    TaskSeminarasResult,
)
from hack4lt.views.account import AdminRequiredMixin, LoginRequiredMixin
from hack4lt.utils import slugify


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

class TaskInfoList(LoginRequiredMixin, ListView):
    model = TaskInfo
    paginate_by = 30
    template_name = 'hack4lt/task_list.html'
    success_url = reverse_lazy('tasks')

    def get_context_data(self, **kwargs):
        context = super(TaskInfoList, self).get_context_data(**kwargs)
        user_tasks = TaskResult.objects.filter(user=self.request.user)
        context['tasks_done'] = dict(user_tasks.filter(done=True).
                                            values_list('task__pk', 'total_points'))
        return context

class TaskInfoDelete(AdminRequiredMixin, DeleteView):
    model = TaskInfo
    success_url = reverse_lazy('tasks')

class TaskResultCreate(UserMixin, CreateView):
    template_name = 'hack4lt/task_result_form.html'
    success_url = reverse_lazy('tasks')

    def get_context_data(self, **kwargs):
        context = super(TaskResultCreate, self).get_context_data(**kwargs)
        context['task'] = TaskInfo.objects.get(slug=self.kwargs.get('slug'))
        return context

    def get_object(self, queryset=None):
        task = TaskInfo.objects.get(slug=self.kwargs['slug'])
        return eval('Task%sResult()' % slugify(unicode(task.slug)).capitalize())

    def form_valid(self, form):
        response = super(TaskResultCreate, self).form_valid(form)
        form.instance.task = TaskInfo.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return response

    def get_form_class(self):
        task = TaskInfo.objects.get(slug=self.kwargs['slug'])
        return eval('Task%sResultForm' % slugify(unicode(task.slug)).capitalize())

class TopicCreate(LoginRequiredMixin, CreateView):
    model = Topic
    success_url = reverse_lazy('topics')

class TopicList(LoginRequiredMixin, ListView):
    model = Topic
    paginate_by = 30
    success_url = reverse_lazy('topics')

class TaskResultUpdate(UserMixin, UpdateView):
    template_name = 'hack4lt/task_result_form.html'
    success_url = reverse_lazy('tasks')

    def get_context_data(self, **kwargs):
        context = super(TaskResultUpdate, self).get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        user = self.request.user
        task_info = TaskInfo.objects.get(slug=slug)
        context['task'] = task_info
        task = TaskResult.objects.get(user=user, task=task_info)
        if task:
            context['comments'] = task.taskcomment_set.all()
        context['comment_form'] = CommentForm()
        return context

    def get_object(self, queryset=None):
        task_slug = self.kwargs.get('slug')
        user = self.request.user
        task_objs = TaskResult.objects.filter(user=user, task__slug=task_slug)
        if not task_objs.exists():
            raise Http404
        task = task_objs.order_by('-created')[0]
        return getattr(task, 'task%sresult' % slugify(unicode(task.task.slug)))

    def form_valid(self, form):
        response = super(TaskResultUpdate, self).form_valid(form)
        form.instance.task = TaskInfo.objects.get(slug=self.kwargs.get('slug'))
        form.save()
        return response

    def get_form_class(self):
        task = TaskInfo.objects.get(slug=self.kwargs['slug'])
        return eval('Task%sResultForm' % slugify(unicode(task.slug)).capitalize())


class TaskResultDetail(UserMixin, DetailView):
    template_name = 'hack4lt/task_result_form.html'
    success_url = reverse_lazy('tasks')

    def get_context_data(self, **kwargs):
        context = super(TaskResultDetail, self).get_context_data(**kwargs)
        context['task'] = TaskInfo.objects.get(slug=self.kwargs.get('slug'))
        return context

    def get_object(self, queryset=None):
        return None


def get_task_form(slug, user):
    task_class = eval('Task%sResult' % slugify(unicode(slug)).capitalize())
    task_result = task_class.objects.order_by('-created').filter(task__slug=slug, user=user)[0]
    task_form_class = eval('Task%sResultForm' % slugify(unicode(slug)).capitalize())
    return task_form_class(instance=task_result)


class TaskResultCheckUpdate(AdminRequiredMixin, UpdateView):
    template_name = 'hack4lt/task_check_form.html'
    success_url = reverse_lazy('tasks')
    form_class = TaskResultForm

    def get_context_data(self, **kwargs):
        context = super(TaskResultCheckUpdate, self).get_context_data(**kwargs)
        slug = self.object.task.slug
        user = self.object.user
        context['task_form'] = get_task_form(slug=slug, user=user)
        context['comments'] = TaskComment.objects.order_by('created').filter(task=self.kwargs.get('pk'))
        context['comment_form'] = CommentForm()
        return context

    def get_object(self, queryset=None):
        return TaskResult.objects.get(pk=self.kwargs.get('pk'))


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


def user_comment_view(request, slug):
    user = request.user
    task_info = TaskInfo.objects.get(slug=slug)
    try:
        task = TaskResult.objects.get(user=user, task=task_info)
    except TaskResult.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            form.instance.user = user
            form.instance.task = task
            form.instance.save()
            return HttpResponseRedirect(reverse_lazy('do-task', kwargs={'slug': slug}))
    else:
        form = CommentForm()
    return HttpResponseRedirect(reverse_lazy('do-task', kwargs={'slug': slug}))


def admin_comment_view(request, pk):
    user = request.user
    task = TaskResult.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            form.instance.user = user
            form.instance.task = task
            form.instance.save()
            return HttpResponseRedirect(reverse_lazy('check-task', kwargs={'pk': pk}))
    else:
        form = CommentForm()
    return HttpResponseRedirect(reverse_lazy('check-task', kwargs={'pk': pk}))


@login_required(login_url=reverse_lazy('login'))
def do_task_view(request, slug):
    user = request.user
    try:
        task = TaskInfo.objects.get(slug=slug)
    except TaskInfo.DoesNotExist:
        raise Http404
    try:
        eval('Task%sResultForm' % slugify(unicode(task.slug)).capitalize())
    except NameError:
        return HttpResponseRedirect(reverse_lazy('view-task', kwargs={'slug': slug}))

    if TaskResult.objects.filter(user=user, task__slug=slug).exists():
        return HttpResponseRedirect(reverse_lazy('update-task', kwargs={'slug': slug}))

    return HttpResponseRedirect(reverse_lazy('create-task', kwargs={'slug': slug}))

