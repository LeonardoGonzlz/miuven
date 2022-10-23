from django.db import models
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import User
# Create your models here.



class indigenas(models.Model):
    autor=models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    cedula=models.CharField(primary_key=True, max_length=11, blank=False)
    nombre=models.CharField(max_length=30, blank=False)
    apellido=models.CharField(max_length=30, blank=False)
    etnia=models.CharField(max_length=30,blank=False)
    casta=models.CharField(max_length=30)
    grado_instruccion=models.CharField(max_length=14, blank=False)
    fecha_de_nacimiento=models.DateField()
    estado_de_salud=models.CharField(max_length=30)
    telefono=models.CharField(max_length=12)
    history = HistoricalRecords()
    class Meta:
        verbose_name='censo de indigena'
    def __str__(self):
        return self.nombre

