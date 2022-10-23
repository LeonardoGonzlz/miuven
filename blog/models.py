from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords
# Create your models here.

class categorias(models.Model):

    nombre=models.CharField(max_length=40)

    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'

    def __str__(self):
        return self.nombre



class puclicaciones(models.Model):
    titulo=models.CharField(max_length=28,blank=False)
    resumen=models.CharField(max_length= 50, blank=False)
    contenido=models.CharField(max_length=3000, blank=False)
    imagen=models.ImageField(upload_to='blog', blank=False, null=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    categorias=models.ManyToManyField(categorias, blank=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name='publicacione'
    
    def __str__(self):
        return self.titulo