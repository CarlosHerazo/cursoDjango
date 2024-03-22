from django.db import models

# Create your models here.

# creamos las tablas heredando la clase Models
class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email = models.EmailField(blank=True, null = True)
    tfno=models.CharField(max_length=10)

    def __str__(self):
        return f'Cliente {self.nombre}'

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=30)
    precio = models.IntegerField()



class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado = models.BooleanField()
