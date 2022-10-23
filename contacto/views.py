from django.shortcuts import render,redirect

from django.core.mail import EmailMessage
from .forms import FormularioContacto
# Create your views here.

def contacto(request):
    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)

        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            mensaje=request.POST.get("mensaje")
            email=request.POST.get("email")

            email=EmailMessage("Prueba", "la persona "+nombre+ "le envio este mensaje"+mensaje,"", 
            ["salazarsekiris@hotmail.com"], reply_to=[email])
            email.send()

            try:
                return redirect("/contacto/?aprovado")
            except:
                return redirect("/contacto/?desaprovado")

    

    return render(request,"contacto/contacto.html",{'formulario_contacto':formulario_contacto})
