from django.shortcuts import render, get_object_or_404
#Importamos el archivo urls para redireccionar
from django.urls import reverse
#Cargamos el formulario
from .forms import ContactForm
#Agregamos las librerias necesarias para trabajr con vistas basadas en clase (CVB)
from django.views.generic.base import TemplateView
#Agregamos la libreria para importar listviews
from django.views.generic.list import ListView
#importamos nuestros modelos
from .models import usuarios,Experiencia,Logros,Habilidades,Educacions

# Create your views here.

#views nos sirve para poder acceder a las plantillas


#funcion de la vista
#def indexfolder(request):
#    return render(request,'core/index.html')

#funcion de nosotros
def nosotrosfolder(request):
    return render(request,'core/nosotros.html')
#def indexfolder(request):
#    return render(request,'core/index.html')
def perfilfolder(request):
    return render(request,'core/perfil.html')

def indexfolder(request):
    #Instanciamos el formulario de contacto
    FormContactame = ContactForm()
    #Validamos que se haya hecho la peticion POST del formulario contacto:
    if request.method == "POST":
        #Re asignamos el valor formcontact, esta vez con todos los datos del formulario
        FormContactame = ContactForm(data=request.POST)
        #Validaremos que todos los campos sean tipo de dato correcto
        if FormContactame.is_valid():
            #retonamos los valores de los campos
            email = request.POST.get('email')
            tipom = request.POST.get('tipom')
            nombre = request.POST.get('nombre')
            msj = request.POST.get('msj')
            #si todo sale bien guardamos y redireccionamos al nombre de la url con un mensaje
            FormContactame.save()
            return redirect(reverse('inicio')+"?Ok")
            #Otra forma de redireccionar
            #return redirect('/indexcore/?OK!')
        #Despues de instanciado lo pasamos en un diccionario de contexto:
    return render(request,'core/index.html',{'formulario': FormContactame})

