from django.shortcuts import render
from django.utils.timezone import now
from .models import Task, Tag
from .forms import TaskForm, LoginForm
from django.contrib.auth import authenticate, login
from django.views import View
from django.contrib import messages

class TaskView(View):

    form = TaskForm
    template_name = 'main.html'

    def context(self, request):
        model = Task.objects.all().order_by('-time').values()
        tags = Tag.objects.values().all()
        context = {'context': list(model), 'form': self.form, 'tags': list(tags)}

        return render(request=request, template_name=self.template_name, context=context)


    def get(self, request):
        return self.context(request)

    
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            try:
                if 'tags' not in request.POST:
                    copy = request.POST.copy()
                    copy['tags'] = '-'
                    f = form.save(commit=False)
                    f.tags = copy['tags']
                    f.time = now().ctime()#.__format__("%b %d %Y - %H:%M")
                    f.save()
                else:
                    f = form.save(commit=False)
                    f.tags = request.POST.getlist('tags')
                    f.time = now().ctime()#.__format__("%b %d %Y - %H:%M")
                    f.save()
            except:
                messages.error(request=request, message='Error on saving entry.')
        else:
            messages.error(request=request, message='Error - invalid form data.') # TODO this is rareoly gonna happen if never.
        return self.get(request)


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
                return render(request, self.template_name, messages.error(request=request, message='Invalid User.'))
            elif user.is_active:
                login(request, user)
                return self.get(request)
            else:
                return render(request, self.template_name, messages.error(request=request, message='Invalid Credentials.'))