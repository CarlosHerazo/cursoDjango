from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos,Pedidos
# Register your models here.

# solo para ver algunos atributos
class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","email","tfno")
    # Agregar casillas de busquedas
    search_fields=("nombre","direccion")


# cramos clase para filtrar articulos
class ArticulosAdmin(admin.ModelAdmin):
    list_display=("nombre","seccion","precio")
    list_filter=("seccion",)


class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero","fecha","entregado")
    #agregar un filtro para fechas
    list_filter=("fecha",)
    date_hierarchy="fecha"


admin.site.register(Clientes,  ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos,PedidosAdmin)
