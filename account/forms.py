from dataclasses import field
from django import forms 
from django.contrib.auth.forms import (UserCreationForm, 
                                        AuthenticationForm,
                                        UsernameField)
from django.contrib.auth import get_user_model
user = get_user_model()

class RegisterForm(UserCreationForm):

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Your Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Your Confirm Password'}))

    class Meta:
        model = user
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': "Your First Name"}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': "Your Last Name"}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                            'placeholder': "Your Email Address"}),
            'username': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': "Your Username"}),
        }

class LoginForm(AuthenticationForm):

    username = UsernameField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Your Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Your Password'}))
