from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from censo_indigena.models import indigenas
# Create your views here.



def home(request):
    if request.user.is_authenticated:
        return redirect("home_username")
    return render(request,"kashi/home.html")

def home_username(request):
    historial_censo = indigenas.history.filter(history_user_id= request.user.pk)
    if request.user.is_authenticated:
        return render(request,"kashi/home_username.html",{"historial":historial_censo})







