from tabnanny import verbose
from django.db import models

class contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return f"{self.name}'s contact message"

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
