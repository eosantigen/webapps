from django.urls import path
# from .views import main, user_login
from .views import TaskView, LoginView

# urlpatterns = [
#   path('', main, name='main'),
#   path('login', user_login, name='login')
# ]

urlpatterns = [
    path('', TaskView.as_view()),
    path('login', LoginView.as_view())
]