# primero Importamos la Clase HTTPResponset
import datetime
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
# Creamos la vista

def saludo(request): # primera vista
    # doc_html = open("plantillaSaludo.html")    
    # cramos un objeto template
    # plt = Template(doc_html.read())
    # doc_html.close()
    fecha = datetime.datetime.now()
    temas_cursos = []
    # cramos el contexto
    datos = {"nombre":"Carlos Herazo","id":"11111","fecha":fecha,"temas":temas_cursos}
    # ctx = Context(datos)
    # doc_html = loader.get_template("plantillaSaludo.html")
    # # pasamos el contexto al obteto template
    # response = doc_html.render(datos)

    return render(request,"plantillaSaludo.html",datos)

def acerca_de(request):
    return render(request,"acerca_de.html",{})

def contactos(request):
    return render(request,"contacto.html",{})