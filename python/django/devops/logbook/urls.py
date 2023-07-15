from django.urls import path
from .views import TaskView, LoginView, LogoutView

urlpatterns = [
    path('', TaskView.as_view(), name='task_view'),
    path('login', LoginView.as_view(), name='login_view'),
    path('logout', LogoutView.as_view(), name='logout_view')
]