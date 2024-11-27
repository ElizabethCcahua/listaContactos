from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    publication_date = models.DateField()
    cover_image = models.ImageField(upload_to='book_covers', null=True, blank=True)

