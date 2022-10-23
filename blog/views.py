from django.shortcuts import render,get_object_or_404,redirect
from blog.models import categorias,puclicaciones
from blog.forms import FormsPuclicaciones
# Create your views here.
print("Hello World")
def blog(request):
    publicacion=puclicaciones.objects.all()
    categoria = categorias.objects.all()
    return render(request,"blog/blog.html",{'publicaciones':publicacion, 'categorias':categoria})


def categoria(request,categoria_id):
    categoria=categorias.objects.get(id=categoria_id)
    publicacion=puclicaciones.objects.filter(categorias=categoria)

    return render(request,"blog/blog.html",{'publicaciones':publicacion})


def crear_publicaciones(request):
    if request.method=='POST':
        form=FormsPuclicaciones(request.POST, request.FILES)
        if form.is_valid():
            puclicaciones=form.save(commit=False)
            puclicaciones.autor=request.user
            puclicaciones.save()
            return redirect("publicacion",pk=puclicaciones.pk)
    else:
        form=FormsPuclicaciones()

    return render(request, 'blog/crear_publicaciones.html',{'form':form})


def publicacion(request, pk):
    publicacion=puclicaciones.objects.filter(pk=pk)
    
    return render(request, 'blog/publicacion.html', {'publicaciones':publicacion})


def editar_publicacion(request, pk):
    publicacion=get_object_or_404(puclicaciones,pk=pk)
    
    if request.method=="POST":
        form=FormsPuclicaciones(request.POST, request.FILES, instance=publicacion)
        if form.is_valid():
            publicaciones=form.save(commit=False)
            publicaciones.save()
    form=FormsPuclicaciones(instance=publicacion)

    return render(request, 'blog/crear_publicaciones.html',{'form':form})
    

def editar_borrar(request):
    autor=request.user.id

    publicacion=puclicaciones.objects.filter(autor=autor)

    return render(request, 'blog/borrar_y_editar.html', {'publicaciones':publicacion})

def borrar_publicacion(request, pk):
    publicacion_borrada=puclicaciones.objects.filter(pk=pk)
    publicacion_borrada.delete()
    
    return redirect('/blog/editar_borrar/?aprovado')

