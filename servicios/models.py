from django.db import models
# Create your models here.

class servicio(models.Model):
    titulo= models.CharField(max_length=30)
    contenido= models.CharField(max_length=40)
    imagen= models.ImageField(upload_to='servicios')
    created= models.DateTimeField(auto_now_add=True)
    update= models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
        
    def __str__(self):
        return self.titulo