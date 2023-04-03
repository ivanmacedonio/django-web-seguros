from .models import Datos
from django.forms import ModelForm
from django import forms 

class DatosForm(forms.ModelForm):

    class Meta:

        model= Datos

        fields = '__all__'
        
        


