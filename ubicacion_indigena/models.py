from django.db import models

# Create your models here.

class Estado(models.Model):
    nombre=models.CharField(max_length=30)
    class Meta:
        verbose_name='estado'
    def __str__(self):
        return self.nombre


class Municipio(models.Model):
    nombre=models.CharField(max_length=30)
    estado=models.ForeignKey(Estado,on_delete=models.CASCADE)
    class Meta:
        verbose_name='municipio'
    def __str__(self):
        return self.nombre

class Parroquia(models.Model):
    nombre=models.CharField(max_length=30)
    municipio=models.ForeignKey(Municipio,on_delete=models.CASCADE)
    class Meta:
        verbose_name='Parroquia'
    def __str__(self):
        return self.nombre

class SectorBarrio(models.Model):
    nombre=models.CharField(max_length=30)
    parroquia=models.ForeignKey(Parroquia,on_delete=models.CASCADE)
    class Meta:
        verbose_name='sector o barrio'
    def __str__(self):
        return self.nombre

class Calle(models.Model):
    nombre=models.CharField(max_length=40)

    class Meta:
        verbose_name='calle'
    def __str__(self):
        return self.nombre

