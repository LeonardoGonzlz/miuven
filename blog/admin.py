from django.contrib import admin
from .models import categorias, puclicaciones
# Register your models here.

class categorias_admin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(categorias, categorias_admin)


class publicaciones_admin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')



admin.site.register(puclicaciones, publicaciones_admin)

