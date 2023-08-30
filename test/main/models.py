from django.db import models

class Book(models.Model):
    isbn = models.IntegerField()
    name = models.CharField(max_length=100)
