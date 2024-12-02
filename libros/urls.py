from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_libro, name='agregar_libro'),
    path('', views.lista_libros, name='lista_libros'),
]
