from django import template
from django.template.defaultfilters import stringfilter
import re

register = template.Library()


@register.filter
@stringfilter
def mitad(contenido, parte):

    num = int(len(contenido) / 6)
    for i in range(50):
        if contenido[num + i] == " ":
            num = num + i +1
            break
    if parte == "primera":
        return contenido[:num]
    
    return contenido[num:]