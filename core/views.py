from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView
from .forms import ContactForm

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def get_success_url(self):
        messages.success(self.request, 'Your message has been successfully sent')
        return super(ContactView, self).get_success_url()