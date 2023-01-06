from django.http import HttpResponse
import datetime


def saludo(request):
    return HttpResponse('Hola mundo, esto es django para toda la ciudad ndea')

def nombre (self,nombre):
    doc = (f'hola, mi nombre es {nombre}')
    return HttpResponse(doc)


from django.template import Template,Context
from django.template import loader

def templato(self):


    nombre = "Ayelen"
    apellido = "Contrera"
    listnotas= [2,5,2,2,5,123,513,4,4]
    fecha = datetime.datetime.now
    datos = {'Nombre':nombre,'Apellido':apellido,"notas":listnotas,"hoy":fecha}


    mihtml = open('C:/Users/UsuarioMda/Desktop/proyecto1/Proyecto1/Proyecto1/plantillas/template.html')
    plantilla = Template(mihtml.read())
    mihtml.close()

    micontexto = Context(datos)
    

    documento = plantilla.render(micontexto)

    return HttpResponse (documento)


def saludo1(request):
    nombre = "Ayelen"
    apellido = "Contrera"
    listnotas= [2,5,2,2,5,123,513,4,4]
    datos = {'Nombre':nombre,'Apellido':apellido,"notas":listnotas}
    
    
    
    plant = loader.get_template('template.html')
    doc = plant.render(datos)
    return HttpResponse(doc)
    