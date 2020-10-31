from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    age = models.PositiveSmallIntegerField(default=0)
    phone = models.CharField(max_length=30, blank=True, null=True)

    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name}'


class GclidClick(models.Model):
    value = models.CharField(max_length=256, unique=True)
