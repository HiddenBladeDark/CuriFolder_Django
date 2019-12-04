#Importamos la libreria form
from django import forms
#creamos una lista de las posibles peticiones del select
from .pqrsf import PQRSF_CHOICES
from django.forms import ModelForm
from .models import Contact


#ESTOS SON CAMPOS DE ENTRADA formato HTML

class ContactForm(forms.ModelForm):
    #widget que tipo de input es
    email=forms.EmailField(label="Correo electronico",widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Ingrese Email'}),required=True)
    tipom = forms.ChoiceField(choices = PQRSF_CHOICES, label="Tipo de atencion requerida",initial = '', widget=forms.Select(attrs=
    {'class':'form-control'}),required=True)
    nombre = forms.CharField(label="Nombre",required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Nombre'}))
    msj = forms.CharField(label="Mensaje",widget=forms.Textarea(attrs={'class':'form-control','rows':'3','placeholder':'Ingrese Mensaje'}), required=True)
    class Meta:
        model = Contact
        fields = "__all__" 
