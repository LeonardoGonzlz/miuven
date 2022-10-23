from django import forms
from .models import indigenas


class IndigenasForm(forms.ModelForm):

    CHOICES=[
    ('primaria',"Primaria"),
    ('segundaria',"Seundaria"),
    ('universitario', "Universitario")
            ]
    grado_instruccion=forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    class Meta:
        model=indigenas
        fields=('cedula','nombre','apellido','etnia','casta',
        'grado_instruccion', 'estado_de_salud','telefono')
        






