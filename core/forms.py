from django import forms 
from .models import contact 

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'

        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control',
                                                    'placeholder': "Your Name"}),
                'email': forms.EmailInput(attrs={'class': 'form-control',
                                                    'placeholder': "Your Email"}),
                'subject': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': "Subject"}),
                'message': forms.Textarea(attrs={'class': 'form-control',
                                                'placeholder': "Message",
                                                'cols': 30,
                                                'rows': 7}),
            }
