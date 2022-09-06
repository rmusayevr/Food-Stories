from django.shortcuts import render

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'user-profile.html')

def change_password(request):
    return render(request, 'change_password.html')
    
def reset_password(request):
    return render(request, 'reset_password.html')
    
def forget_password(request):
    return render(request, 'forget_password.html')