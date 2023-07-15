from django.shortcuts import render, redirect
from .models import Task, Tag
from .forms import TaskForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskView(LoginRequiredMixin, View):

    form = TaskForm
    template_name = 'main.html'
    
    def context(self, request):
        model = Task.objects.all().values()
        tags = Tag.objects.values().all()

        for timestamp in model:
            timestamp['time'] = str(timestamp.get('time')).replace('T', ' ')
        context = {'context': list(model), 'form': self.form, 'tags': list(tags)}

        return render(request=request, template_name=self.template_name, context=context)
    
    def get(self, request):
        return self.context(request)

    def post(self, request):
        form = self.form(request.POST)
        form.instance.user = request.user
        if form.is_valid():
            try:
                if 'tags' not in request.POST:
                    copy = request.POST.copy()
                    copy['tags'] = '-'
                    f = form.save(commit=False)
                    f.tags = copy['tags']
                    print(f.tags)
                    f.save()
                else:
                    f = form.save(commit=False)
                    f.tags = request.POST.getlist('tags')
                    f.save()
            except Exception as exception:
                print(exception) # TODO change to logging module.
                messages.error(request=request, message='Error on saving entry.')
        else:
            messages.error(request=request, message='Error - invalid form data.') # TODO this is rarely gonna happen if never.
        return redirect(to='task_view')


class LoginView(View):

    form = LoginForm
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            user = authenticate(request, username=clean_data['username'], password=clean_data['password'])
            if user is None:
                return render(request, self.template_name, messages.error(request=request, message='Non-existent User.'))
            elif user.is_active:
                login(request, user)
                return redirect(to='task_view')
            else:
                return render(request, self.template_name, messages.error(request=request, message='Invalid Credentials.'))
            
            
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(to='login_view')