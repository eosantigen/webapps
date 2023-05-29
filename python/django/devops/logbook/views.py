from django.shortcuts import render, redirect, HttpResponse
from django.utils.timezone import now
from .models import Task, Tag
from .forms import TaskForm, LoginForm
from django.contrib.auth import authenticate, login
from django.views import View
from django.contrib import messages

class TaskView(View):

    form = TaskForm
    template_name = "main.html"

    def get(self, request):

        model = Task.objects.all().order_by('-time').values()
        tags = Tag.objects.values().all()
        context = {'context': list(model), 'form': self.form, 'tags': list(tags)}

        return render(request=request, template_name=self.template_name, context=context)

    
    def post(self, request):

        form = self.form(request.POST)
        if form.is_valid():
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
        else:
            messages.error(request=request, message='Error: Too long task description.') # TODO - fix on the model side sync
        return redirect('/logbook')


# def user_login(request):

#     print(request.method, request.body, request.get_host(), request.get_full_path())
    
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             clean_data = form.cleaned_data
#             user = authenticate(request, username=clean_data['username'], password=clean_data['password'])
#             if user is None:
#                 return render(request, 'login.html', {'user': 'invalid user'})
#             elif user.is_active:
#                 login(request, user)
#                 return main(request)
#             else:
#                 return render(request, 'login.html', {'user': 'invalid - please check your credentials'})
#     else:
#         form = LoginForm()
#         return render(request, 'login.html', {'login_form': form})