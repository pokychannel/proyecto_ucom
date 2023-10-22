from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    direccion = models.TextField()

class Cuenta(models.Model):
    TIPO_CUENTA = [
        ('CC', 'Cuenta Corriente'),
        ('CA', 'Caja de Ahorro'),
    ]
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    tipo_cuenta = models.CharField(max_length=2, choices=TIPO_CUENTA)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class CuentaCorriente(models.Model):
    cuenta = models.OneToOneField(Cuenta, on_delete=models.CASCADE)
    limite_sobregiro = models.DecimalField(max_digits=10, decimal_places=2)

class CajaAhorro(models.Model):
    cuenta = models.OneToOneField(Cuenta, on_delete=models.CASCADE)
    tasa_interes = models.DecimalField(max_digits=5, decimal_places=2)

class Movimiento(models.Model):
    TIPO_MOVIMIENTO = [
        ('D', 'Depósito'),
        ('R', 'Retiro'),
        ('T', 'Transferencia'),
    ]
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    tipo_movimiento = models.CharField(max_length=1, choices=TIPO_MOVIMIENTO)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()