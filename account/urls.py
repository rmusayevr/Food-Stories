from django.urls import path
from .views import register, login, profile, change_password, reset_password, forget_password

urlpatterns = [
    path('register/', register, name = 'register'),
    path('login/', login, name = 'login'),
    path('profile/', profile, name = 'profile'),
    path('change_password/', change_password, name = 'change_password'),
    path('reset_password/', reset_password, name = 'reset_password'),
    path('forget_password/', forget_password, name = 'forget_password')
]