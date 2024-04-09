from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _


"""Model represents a user of the webapp"""
class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [email]

    objects = CustomUserManager()

    def __str__(self):
        return self.email