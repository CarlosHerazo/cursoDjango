# Request: para realizar peticiones
# HttpResponse: Para enviar la respuesta usando el protocolo HTTP

from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, apellido,edad):
        self.nombre= nombre
        self.apellido= apellido
        self.edad= edad



def saludo(request):  # primera vista, devuelve una respuesta con el texto
    p1= Persona("Juan","Herazo",19)
    fecha_actual=datetime.now().date()
    #doc_externo=open("C:/Users/carhe/OneDrive/Escritorio/ProyectosDjango/proyecto1/proyecto1/plantilla/miplantilla.html")
    #plt = Template(doc_externo.read())
    #doc_externo.close()

   
    temas_cursos = ["python","Django","SQLITE3","MVT","Formularios","Plantillas","Despliegues"]
   
    #ORDEN DE LLAMADAS
    # DICCIONARIOS
    # ATRIBUTOS
    # METODOS
    # LISTAS
   # pasar variablezs a las plantillas
   # doc_externo = loader.get_template("miplantilla.html")
   # ctx = Context({"nombre":p1.nombre,"edad":p1.edad,"fecha":fecha_actual, "temas": temas_cursos })
   # document = doc_externo.render({"nombre":p1.nombre,"edad":p1.edad,"fecha":fecha_actual, "temas": temas_cursos })

    return render(request,"miplantilla.html",{"nombre":p1.nombre,"edad":p1.edad,"fecha":fecha_actual, "temas": temas_cursos })

def cursoC(request):
    fecha_actual=datetime.now().date()

    return render(request,"CursosC.html",{"fecha":fecha_actual})

def cursoCss(request):
    fecha_actual=datetime.now().date()
    return render(request,"CursosCss.html",{"fecha":fecha_actual})