from django.db import models
from accounts.models import Usuario

class Pet(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='mascotas/')
    phone_1 = models.CharField(max_length=15)
    phone_2 = models.CharField(max_length=15, null=True, blank=True)
    adress = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    usuario = models.ForeignKey(Usuario, 
                             on_delete=models.CASCADE, 
                             related_name="pets")
