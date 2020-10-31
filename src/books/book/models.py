from django.db import models


class Book(models.Model):
    author = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    year = models.PositiveSmallIntegerField(default=1900)
    users = models.ForeignKey('user.User', related_name='books', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', related_name='book', on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=128)
