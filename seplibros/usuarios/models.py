from django.db import models

from .managers import UsuarioManager

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.
class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = UsuarioManager()

    def __str__(self):
        return self.username