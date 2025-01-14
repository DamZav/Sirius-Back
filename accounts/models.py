from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False) # Activación tras el pago


# Autenticación social: Integra django-allauth para login con Google/Facebook. 
# Instala el paquete:
# pip install django-allauth
