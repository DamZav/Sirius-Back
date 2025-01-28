from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False) # Activación tras el pago

    #  Solución a que chocaba: Cambiar el related_name de las relaciones 
    # inversas
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Cambia el nombre inverso
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Cambia el nombre inverso
        blank=True
    )

# Autenticación social: Integra django-allauth para login con Google/Facebook. 
# Instala el paquete:
# pip install django-allauth
