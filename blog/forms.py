from django import forms
from .models import puclicaciones

class FormsPuclicaciones(forms.ModelForm):
    contenido=forms.CharField(min_length=40, widget=forms.Textarea)

    class Meta:
        model=puclicaciones
        fields=('categorias','titulo','imagen','resumen','contenido')