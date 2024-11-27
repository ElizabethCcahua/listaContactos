from django.contrib import admin

# Register your models here.
from .models import Book, Review  # nombre del modelo

# Registro simple de los modelos
admin.site.register(Book)
admin.site.register(Review)
