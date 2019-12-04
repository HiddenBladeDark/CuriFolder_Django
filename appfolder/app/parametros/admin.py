from django.contrib import admin

# Register your models here.

#importamos cada una de las clases creadas en el archivo models.py

from .models import Etnia
from .models import TipoDocu
from .models import EstaCivil
from .models import tipoEstu
from .models import tipoLogr
from .models import Empleos
from .models import Contact

#importamos los modelos crados en models.py
from .models import usuarios,Experiencia,Educacions,Habilidades,Experiencia,Logros

class UsuariosModelAdmin(admin.ModelAdmin):
    #Indicamos que columnas deseamos ver
    list_display = ("__str__","idUsuario","ImageUsua","EstaUsua")
    #Agregamos una barra de busqueda:
    search_fields = ('IdUsuario','GeneUsua','CeluUsua','TeleUsua',)
    #Agregamos filtros
    list_filter = ('idUsuario','GeneUsua',)
    #Mostramos las fechas de creacion del usuario:
    readonly_fields = ('RegisUsua',)
    #Indicamos desde donde se obtienen estos parametros

    class Meta:
        model = usuarios
admin.site.register(usuarios, UsuariosModelAdmin)


class ExperienciaModelAdmin(admin.ModelAdmin):
    #Indicamos que columnas deseamos ver
    list_display = ("__str__","CarExpe","EmprExpe","FechIn","FechFin","SopoExpe")
    #Agregamos una barra de busqueda:
    search_fields = ('CarExpe','EmprExpe',)
    #Agregamos filtros
    list_filter = ('CarExpe','FechFin',)
    #Mostramos las fechas de creacion del usuario:
    readonly_fields = ('EstaExpt',)
    #Indicamos desde donde se obtienen estos parametros

    class Meta:
        model = Experiencia

admin.site.register(Experiencia, ExperienciaModelAdmin)


class EducacionModelAdmin(admin.ModelAdmin):
    #Indicamos que columnas deseamos ver
    list_display = ("__str__","TipoEstu","TituloEst","FechGrado","Instituto","SoporteEs")
    #Agregamos una barra de busqueda:
    search_fields = ('TituloEst','TipoEstu',)
    #Agregamos filtros
    list_filter = ('TipoEstu','FechGrado',)
    #Mostramos las fechas de creacion del usuario:
    readonly_fields = ('EstaEstu',)
    #Indicamos desde donde se obtienen estos parametros

    class Meta:
        model = Educacions
admin.site.register(Educacions, EducacionModelAdmin)




class HabilidadesModelAdmin(admin.ModelAdmin):
    #Indicamos que columnas deseamos ver
    list_display = ("__str__","NombHabil","NiveHabi")
    #Agregamos una barra de busqueda:
    search_fields = ('NombHabil','NiveHabi',)
    #Agregamos filtros
    list_filter = ('NiveHabi','NombHabil',)
    #Mostramos las fechas de creacion del usuario:
    #readonly_fields = ('EstaEstu',)
    #Indicamos desde donde se obtienen estos parametros

    class Meta:
        model = Habilidades
admin.site.register(Habilidades, HabilidadesModelAdmin)





admin.site.register(Etnia)
admin.site.register(TipoDocu)
admin.site.register(EstaCivil)
admin.site.register(tipoEstu)
admin.site.register(tipoLogr)
admin.site.register(Empleos)
admin.site.register(Contact)



#Agregamos la clase Model. ModelAdmin para modificar la vista a cada uno modelos importados


#class EtniaModelAdmin(admin.ModelAdmin):
    #Indicamos que columnas queremos ver
    #columnas que deseamos editar
#    list_display = ["NombEtni"]
    #agregamos una barra de busqueda
#    search_fields = ["NombEtni"]
    #podemos agregar un filtro
#    list_filter = ["NombEtni"]

#    class Meta:
#        model = Etnia
#admin.site.register(Etnia)

