from django.db import models
from accounts.models import Usuario

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=50)
    pagado = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    usuario = models.ForeignKey(Usuario, 
                                on_delete=models.SET_NULL, 
                                null=True)

# Integrar PayPal y Mercado Pago: Usa paquetes como paypalrestsdk o la API 
# oficial de Mercado Pago. 