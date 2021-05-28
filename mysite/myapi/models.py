from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self) -> CharField:
        return self.name
