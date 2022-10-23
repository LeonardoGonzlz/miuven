from django.shortcuts import render,redirect,get_object_or_404
from .models import indigenas
from .forms import IndigenasForm
# Create your views here.

def censar(request):

    indigenas_censados = indigenas.objects.filter(autor=request.user)

    if request.method=="POST":
        form = IndigenasForm(request.POST)
        if form.is_valid():
            censo = form.save(commit=False)
            censo.fecha_de_nacimiento = request.POST.get("fecha-nacimiento")
            censo.autor = request.user
            censo.save()
            return redirect('censo_indigena/censar/?aprovado')
    else:
        form= IndigenasForm()
    return render(request, 'censo_indigena/censo_indigenas.html', {'form':form,"censados":indigenas_censados})


def borrar_indigena(request, cedula):
    indigena_a_borrar=indigenas.objects.filter(cedula=cedula)
    indigena_a_borrar.delete()
    
    return redirect('censo_indigena/censar/?aprovado')

def editar_indigena(request, cedula):
    indigena=get_object_or_404(indigenas,cedula=cedula)
    indigenas_censados = indigenas.objects.filter(autor=request.user)
    if request.method=="POST":
        form=IndigenasForm(request.POST, instance=indigena)
        if form.is_valid():
            censo = form.save(commit=False)
            censo.autor = request.user
            censo.fecha_de_nacimiento = request.POST.get("fecha-nacimiento")
            censo.save()
            return redirect('censo_indigena/censar/?aprovado')
            
    form=IndigenasForm(instance=indigena)

    return render(request, 'censo_indigena/censo_indigenas.html', {'form':form,"censados":indigenas_censados})
