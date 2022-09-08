from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser


class user(AbstractUser):
    image = models.ImageField(upload_to='profile_images')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"