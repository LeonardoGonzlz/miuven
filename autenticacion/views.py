from django.shortcuts import render,redirect

from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
# Create your views here.

class Vregistrarse(View):

    def get(self,request):
        form=UserCreationForm()
        return render(request, "autenticacion/registrarse.html",{"form":form})
    
    def post(self,request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            usuario=form.save()
            login(request, usuario)
            return redirect("home_username")
        else:
            return redirect("/autenticacion/iniciar_seccion/?desaprovado")


def iniciar_seccion(request):

    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)

        if form.is_valid():
            nombre=form.cleaned_data.get("username")
            contraseña=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre,password=contraseña)

            if usuario is not None:
                login(request,usuario)
                return redirect("home_username")
            else:
                return redirect("/autenticacion/iniciar_seccion/?desaprovado")
        else:
            return redirect("/autenticacion/iniciar_seccion/?desaprovado")

    form=AuthenticationForm()
    return render(request, "autenticacion/iniciar_seccion.html",{"form":form})


def cerrar_seccion(request):
    logout(request)

    return redirect("home")