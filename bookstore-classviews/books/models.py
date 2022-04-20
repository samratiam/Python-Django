
from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
