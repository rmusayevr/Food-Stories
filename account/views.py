from email import message
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import (PasswordChangeView, 
                                        PasswordResetView, 
                                        PasswordResetConfirmView, 
                                        LoginView)
from django.utils.encoding import force_str, force_bytes
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_decode
from .tokens import account_activation_token
from django.contrib import messages
from .forms import RegisterForm, LoginForm, ResetPasswordForm, CustomSetPasswordForm, ChangePasswordForm
from .models import user
from Food_Stories.settings import EMAIL_HOST_USER
from django.contrib.messages.views import SuccessMessageMixin



class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(RegisterView, self).dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            User = form.save(commit=False)
            User.is_active = False
            User.save()

            subject = "Activate Your Account"
            current_site = get_current_site(request)
            message = render_to_string('confirmation_email.html', {
                'user': User,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(User.pk)),
                'token': account_activation_token.make_token(User),
            })
            from_email = EMAIL_HOST_USER
            to_email = request.POST['email']
            send_mail(subject, message, from_email, [to_email, ])
            messages.success(self.request, 'We sent Confirmation Email !')

            return redirect('login')
        return render(request, self.template_name, {'form': form})

def activate(request, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    User = user.objects.filter(pk=uid, is_active=False).first()

    if User is not None and account_activation_token.check_token(User, token):
        messages.success(request, 'Your profile is activated')
        User.is_active = True
        User.save()
        return redirect('login')
    else:
        messages.error(request, 'Your session is expired')
        return redirect('/')

class LogInView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    # authentication_form = LoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(LogInView, self).dispatch(request, *args, **kwargs)

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'reset_password.html'
    form_class = ResetPasswordForm
    email_template_name = 'reset_password_email.html'
    subject_template_name = 'reset_password_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      "If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('home')
    
    def get_success_url(self):
        messages.success(self.request, 'Your request to change your password has been registered. Please check your email.')
        return super(ResetPasswordView, self).get_success_url()

class ResetPasswordConfirmView(PasswordResetConfirmView):
    template_name='reset_password_confirm.html', 
    form_class=CustomSetPasswordForm,
    success_url = reverse_lazy('reset_password_complete')

    def get_success_url(self):
        messages.success(self.request, 'Your password has been successfully changed')
        return super(ResetPasswordConfirmView, self).get_success_url()

class ChangePasswordView(PasswordChangeView):
    template_name='change_password.html',
    form_class=ChangePasswordForm,
    success_url = reverse_lazy('home')

    def get_success_url(self):
        messages.success(self.request, 'Your password has been successfully changed')
        return super(ChangePasswordView, self).get_success_url()


def profile(request):
    return render(request, 'user-profile.html')

def change_password(request):
    return render(request, 'change_password.html')
    
def reset_password(request):
    return render(request, 'reset_password.html')
    
def forget_password(request):
    return render(request, 'forget_password.html')