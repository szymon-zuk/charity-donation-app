from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=64)

TYPES = [
    ("Fundacja", "FA"),
    ("Organizacja pozarządowa", "OP"),
    ("Zbiórka lokalna", "ZL")
]

class Institution(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    type = models.CharField(choices=TYPES, max_length=2, default=TYPES[0][0])
    categories = models.ManyToManyField(Category)