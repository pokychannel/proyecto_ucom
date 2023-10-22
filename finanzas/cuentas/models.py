from django.db import models

class Cuenta(models.Model):
    TIPOS = (
        ('CC', 'Cuenta Corriente'),
        ('CA', 'Caja de Ahorro'),
    )
    MONEDA = (
        ('USD', 'Dólar'),
        ('PYG', 'Guaranies'),
    )
    titular = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tipo = models.CharField(max_length=2, choices=TIPOS)
    moneda = models.CharField(max_length=3, choices=MONEDA)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    activa = models.BooleanField(default=True)

class Transaccion(models.Model):
    cuenta_origen = models.ForeignKey(Cuenta, related_name="origenes", on_delete=models.CASCADE)
    cuenta_destino = models.ForeignKey(Cuenta, related_name="destinos", on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
