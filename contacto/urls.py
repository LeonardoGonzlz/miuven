from django.urls import path

from contacto import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('', views.contacto, name="contacto")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)