from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.validators import MinLengthValidator, MaxLengthValidator
# Create your models here.

def rut_validator(value):
    if not value[-2] == "-":
        raise ValidationError("El rut debe cumplir con el siguiente formato: 12345678-3")
    if len(value) != 10:
        raise ValidationError("El rut debe tener 10 caracteres")

class Cuenta(models.Model):
    rut = models.CharField(primary_key=True, null=False, max_length=10, validators=[rut_validator], error_messages={"invalid": "Debe ingresar rut"})    
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    saldo=models.IntegerField(null=False, default=50000)
    
class Productos(models.Model):
    id_prod=models.IntegerField(primary_key=True, null=False, error_messages="Debe ingresar el id del producto")
    nombre_producto=models.CharField(max_length=50, null=False)
    precio=models.IntegerField(null=False)
    
class Pedidos(models.Model):
    id_pedido=models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=50, validators=[MinLengthValidator(4, message='El nombre es demasiado corto.')])
    direccion = models.CharField(max_length=50, null=False, validators=[MinLengthValidator(5, message='direccion invalida, debe ingresar una direccion correcta.')])