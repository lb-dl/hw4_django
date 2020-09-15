from django.db import models


class Book(models.Model):
    author = models.CharField(max_length=128)
    title = models.CharField(max_length=128, unique=True)
    year = models.PositiveSmallIntegerField(default=1900)
