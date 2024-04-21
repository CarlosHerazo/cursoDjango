from django.shortcuts import render
from django.http import HttpResponse
from GestionPedidos.models import Articulos
# Create your views here.

def busqueda_productos(request):
    return render(request, "busqueda_pedido.html")

def buscar(request):
    if request.GET['prd']:
       # mensaje = f"Articulo buscado: {request.GET['prd']}" 
       prd = request.GET['prd']
       art = Articulos.objects.filter(nombre__icontains=prd) # devuelve una lista de la primera cadena que coincidan con la busqueda
       print(art)
       return render(request, "resultados_busqueda.html",{"articulos":art,"query":prd})
    else :
        mensaje = "No hay ningun mensaje"
    
    return HttpResponse(mensaje)
