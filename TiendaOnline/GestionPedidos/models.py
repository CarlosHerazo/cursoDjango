from django.db import models

# Create your models here.

#  tabla cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="nombre_cliente")
    direccion = models.CharField(max_length=50, verbose_name="direccion_cliente")
    email = models.EmailField(blank=True, null=True, verbose_name="email_cliente") # opcional
    tlf = models.CharField(max_length=50,  verbose_name="telefono_cliente")

    def __str__(self):
        return self.nombre

# tablas articulos
class Articulos(models.Model):
    nombre = models.CharField(max_length=50)
    seccion = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre

# tablas pedidos
class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
