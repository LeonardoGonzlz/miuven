from django.urls import path
from censo_indigena.views import censar,borrar_indigena,editar_indigena

urlpatterns=[
    path('censar/', censar, name='censar'),
    path('borrar_indigena/<cedula>', borrar_indigena, name="borrar_indigena"),
    path('editar_indigena/<cedula>', editar_indigena, name="editar_indigena")
]