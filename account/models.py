from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy


class user(AbstractUser):
    image = models.ImageField(upload_to='profile_images')
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse_lazy('profile', kwargs={'pk':self.pk})

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"