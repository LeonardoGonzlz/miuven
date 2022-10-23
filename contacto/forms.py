from django import forms

class FormularioContacto(forms.Form):
    nombre=forms.CharField(max_length=30,label='Nombre', required=True)
    email=forms.EmailField(required=True, label='Email')
    mensaje=forms.CharField(widget=forms.Textarea, label='mensaje')

