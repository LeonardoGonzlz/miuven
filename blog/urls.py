from django.urls import path

from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.blog, name="blog"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),
    path('publicar/', views.crear_publicaciones, name='publicar'),
    path('publicacion/<int:pk>/', views.publicacion, name='publicacion'),
    path('editar_publicacion/<int:pk>/', views.editar_publicacion, name='editar_publicacion'),
    path('editar_borrar/', views.editar_borrar, name='editar_borrar'),
    path('borrar_publicacion/<pk>', views.borrar_publicacion, name='borrar_publicacion')
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

