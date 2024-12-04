from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_libro, name='agregar_libro'),
    path('review/<int:libro_id>/', views.agregar_review, name='agregar_review'),
    path('detalle/<int:libro_id>/', views.detalle_libro, name='detalle_libro'),  # Nueva URL para el detalle
    path('', views.lista_libros, name='lista_libros'),
]
