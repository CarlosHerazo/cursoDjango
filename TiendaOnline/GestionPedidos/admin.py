from django.contrib import admin
from GestionPedidos.models import Cliente,Articulos,Pedidos

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","email","tlf")
    search_fields=("nombre","email") # input para buscar

class ArticulosAdmin(admin.ModelAdmin):
    list_filter=("seccion",)

class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero","fecha")
    list_filter=("fecha",)

#Agregar las tablas en admin
admin.site.register(Cliente, ClientesAdmin)

admin.site.register(Articulos, ArticulosAdmin)

admin.site.register(Pedidos, PedidosAdmin)

