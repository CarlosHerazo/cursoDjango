# primero Importamos la Clase HTTPResponset
import datetime
from django.http import HttpResponse
from django.template import Template, Context

# Creamos la vista

def saludo(request): # primera vista
    doc_html = open("Proyecto1/plantillas/plantillaSaludo.html") 
    
    # cramos un objeto template
    plt = Template(doc_html.read())
    doc_html.close()
    fecha = datetime.datetime.now()
    # cramos el contexto
    datos = {"nombre":"Carlos Herazo","id":"11111","fecha":fecha}
    ctx = Context(datos)

    # pasamos el contexto al obteto template

    response = plt.render(ctx)

    return HttpResponse(response)

def despedida(request): # segunda vista

    return HttpResponse("Chao compañeros")

def fechaHoy(request):  #tercera vista
    fecha_actual = datetime.datetime.now()
    
    response =f"""
            <html>
                <body>
                    <h1>
                        la fecha de hoy es: {fecha_actual}
                    </h1>
                </body>
            </html>

            """
    return HttpResponse(response)  # cuarta vista


def edad(request, agno, edad, agnoActual):  # quinta vista
    periodo = agno-agnoActual
    edadFutura = (edad) + periodo
    fecha_actual = datetime.datetime.now()
    
    response =f"""
            <html>
                <body>
                    <h1>
                        Actualmente tiene {edad}, y en el año {agno} tendras {edadFutura} años
                    </h1>
                </body>
            </html>

            """
    return HttpResponse(response)


