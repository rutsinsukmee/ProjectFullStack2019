from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Binding(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    isbn_10 = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    binding = models.ForeignKey(Binding, on_delete= models.SET_NULL, null=True)
    year = models.PositiveSmallIntegerField()
    publisher = models.ForeignKey(Publisher, on_delete= models.SET_NULL, null=True)
    isavailable = models.BooleanField()

    def __str__(self):
        return self.title

class Borrow(models.Model):
    borrower = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    book = models.ForeignKey(Book, on_delete= models.SET_NULL, null=True)

    def __str__(self):
        return str(self.borrower)


class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete= models.SET_NULL, null=True)
    actor = models.ForeignKey(User, on_delete=models.PROTECT)
    action = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.book)