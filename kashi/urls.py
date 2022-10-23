from django.urls import path

from kashi import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('home_username/', views.home_username, name='home_username')
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)