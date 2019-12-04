from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings
#Importamos la lista de tipos de mensajes:
from .pqrsf import PQRSF_CHOICES
#from parametros.models import TipoDocu, Etnia, EstaCivil, Empleos, tipoLogr, tipoEstu
# Create your models here.

# los modelos son una clase devuelve un objeto
#por lo que crearemos una clase con el nombre de la entidad o coleccion y definiremos los atributos
# Modelos son clase

#clase usuario
class usuarios(models.Model):
    idUsuario =models.CharField(max_length = 50, verbose_name = "N. Identificacion",default="")
    idTipoDocu = models.ForeignKey('parametros.TipoDocu', default="", on_delete=models.CASCADE,verbose_name="Tipo de Documento")
    idEstaCivil = models.ForeignKey('parametros.EstaCivil', default="",on_delete=models.CASCADE,verbose_name="Estado Civil")
    idEtnias = models.ForeignKey('parametros.Etnia', default="", on_delete=models.CASCADE, verbose_name="Etnias")
    ImageUsua = models.ImageField(verbose_name = "Foto de Perfil", upload_to = "perfiles/img")
    PerfilPro = RichTextField(default="Candidato...", verbose_name = "perfil profesional")
    GeneUsua = models.CharField(max_length = 1, default="O",verbose_name = "Genero")
    TeleUsua = models.CharField(max_length = 20, default="0", verbose_name = "Telefono")
    CeluUsua = models.CharField(max_length = 20, default="0",verbose_name = "Celular")
    DireUsua = models.DateTimeField(default="0",verbose_name = "Direccion Postal")
    RegisUsua = models.DateTimeField(default=0, auto_now_add = False, verbose_name = "Registrado el :")
    EstaUsua = models.CharField(max_length = 50, default="Activo", verbose_name= "Estado")

    class Meta:
        verbose_name = "Candidato"
        verbose_name_plural = "Candidatos"

    #Ya creada la case, retornamos el objeto NomEtni o Nombre de Etnia


    def __str__(self):
        return self.idUsuario


#clase Experiencia

class Experiencia(models.Model):
    #Atributos de la clase experiencia
    CarExpe = models.ForeignKey('parametros.Empleos', on_delete=models.CASCADE, limit_choices_to={'EsCargo': 'SI'}, verbose_name="Cargo Ocupado")
    EmprExpe = models.CharField(max_length = 150, verbose_name = "Empresa")
    TeleEmpr = models.CharField(max_length = 30, verbose_name = "Telefono de contacto de la empresa")
    JefeExpe = models.CharField(max_length = 30, verbose_name = "Persona de contacto de la empresa")
    FechIn = models.DateTimeField(auto_now_add = False, default = "0", verbose_name = "Fecha de inicio")
    FechFin = models.DateTimeField(auto_now_add = False, default = "0", verbose_name = "Fecha de terminacion")
    FuncionE = RichTextField(verbose_name = "Funciones desempeñadas")
    LogrExpe = RichTextField(verbose_name = "Logros Alcanzados")
    SopoExpe = models.FileField(upload_to="soportes/laboral", default="", verbose_name = "Certificado Laboral")
    EstaExpt = models.CharField(max_length = 30, default="Activo", verbose_name = "Estado de Experiencia")


    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencia Laboral"

#Retornamos id cargexpe de clase experiencia
    def __str__(self):
        return self.CarExpe



#Clase para alamcenar la educacion del candidato
class Educacions(models.Model):
    TipoEstu = models.ForeignKey('parametros.TipoEstu', on_delete=models.CASCADE,default="", verbose_name="Tipo de Educacion")
    Instituto = models.CharField(max_length=30, default = "Activo", verbose_name="Institucion o Academia")
    TituloEst = models.CharField(max_length=250, verbose_name = "Titulo Obtenido")
    FechGrado = models.DateTimeField(auto_now_add = False, default=0, verbose_name = "Fecha de Graduacion")
    SoporteEs = models.FileField(upload_to = "Soporte/educacion", default = "", verbose_name="Soporte Educacion")
    EstaEstu = models.CharField(max_length = 30, default="Activo", verbose_name="Estado de Educacion")


    class Meta:
        verbose_name = "Educacion"
        verbose_name_plural = "Estudios Registrados"

    #Retornamos TipoEstu est de clas educacions
    def __str__(self):
        return self.TipoEstu

#Clase para almacenar los logros obtenidos

class Logros(models.Model):
    NombTilo = models.ForeignKey('parametros.TipoLogr', on_delete=models.CASCADE, verbose_name="Tipo de logro")
    FechLogr = models.DateTimeField(auto_now_add = False,default=0,verbose_name="Fecha de Culminacion de logro")
    NomLogr = models.CharField(max_length = 100, default="Activo",verbose_name="Logro o Disticion")
    DescLogr = RichTextField(verbose_name = "Descripcion o caracteristicas del Logro")

    class Meta:
        verbose_name = "Logros"
        verbose_name_plural = "Logros Obtenidos"

    #Retornamos el Nomlogr de clase logros
    def __str__(self):
        return self.NomLogr


class Habilidades(models.Model):
    NombHabil = models.CharField(max_length = 100, default = "Activo", verbose_name="Habilidad")
    NiveHabi = models.CharField(max_length = 20, default="Activo", verbose_name="Nivel de Habilidad:")


    class Meta:
        verbose_name = "Habilidades"
        verbose_name_plural = "Habilidades y competencias"

#Retornamos NombHabil de la clase models
    def __str__(self):
        return self.NombHabil




#clase mensajes
class Contact(models.Model):
    email = models.EmailField(default= 'admin@admin.com', max_length = 50, verbose_name = "Correo electronico")
    tipoem = models.CharField(max_length = 50, choices=PQRSF_CHOICES, default="Peticion",verbose_name="Categoria")
    nombre = models.CharField(default= 'Hola', max_length = 250, verbose_name = "Nombre")
    msj = RichTextField(default = 'Quisiera', verbose_name = "Mensaje")


class Meta:
    verbose_name = "Mensaje PQRSF"
    verbose_name_plural = "Mensaje PQRSF"



#clase para el modelo Etnia
class Etnia(models.Model):
    NombEtni = models.CharField(max_length = 50,verbose_name="Grupo Etnico")

    
    class Meta:
        verbose_name="Grupo Etnia"
        verbose_name_plural="Grupos Etnia"


    #Ya creada la clase, retornamos el objeto NombEtni, o nombre de etnia
    def __str__(self):
        return self.NombEtni


#Agregamos las otras clases del modulo:


#Clase para el modelo tipodocu:
class TipoDocu(models.Model):
    NombtiDo = models.CharField(max_length=50,verbose_name="Tipo de Documento")

    class Meta:
        verbose_name="Documento"
        verbose_name_plural="Documentos"


    def __str__(self):
        return self.NombtiDo


#Clase para el modelo EstaCivil o estado civil:
class EstaCivil(models.Model):
    nombEsci = models.CharField(max_length = 50,verbose_name="Estado Civil")

    class Meta:
        verbose_name="Estado Civil"
        verbose_name_plural="Estados Civiles"


    def __str__(self):
        return self.nombEsci

#Clase para el modelo tipo logr o tipos de logro:
class tipoLogr(models.Model):
    NombTilo = models.CharField(max_length = 50,verbose_name="Tipo de logro")

    class Meta:
        verbose_name="Logros"
        verbose_name_plural="Logros obtenidos"

    def __str__(self):
        return self.NombTilo

#Clase para el modelo  tipo estudiante
class tipoEstu(models.Model):
    NombTi = models.CharField(max_length = 50,verbose_name="Tipo Estudiante")
    

    class Meta:
        verbose_name="Estudiante"
        verbose_name_plural="Estudiantes"

    def __str__(self):
        return self.NombTi

class Empleos(models.Model):
    EmpNom = models.CharField(max_length = 50,verbose_name="Experiencia")
    

    class Meta:
        verbose_name="Cargo"
        verbose_name_plural="Cargos"

    def __str__(self):
        return self.EmpNom

