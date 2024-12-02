from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_libro, name='agregar_libro'),
    path('review/<int:libro_id>/', views.agregar_review, name='agregar_review'),
    path('', views.lista_libros, name='lista_libros'),
]
