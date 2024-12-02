from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('register/', views.register, name='register'),
    path('admin/', admin.site.urls),
    path('libros/', include('libros.urls')),
    path('personas/', include('personas.urls')),
]