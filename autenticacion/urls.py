from django.urls import path

from autenticacion.views import iniciar_seccion,Vregistrarse,cerrar_seccion


urlpatterns=[
    
    path("iniciar_seccion/", iniciar_seccion, name="iniciar_seccion"),
    path("registrarse/", Vregistrarse.as_view(), name="registrarse"),
    path("cerrar_seccion", cerrar_seccion, name="cerrar_seccion")

]

