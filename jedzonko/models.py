from django.db import models


# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=256)
    ingredients = models.TextField(max_length=1024)
    description = models.TextField(max_length=2048)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    preparation_time = models.PositiveSmallIntegerField()
    way_of_preparing = models.TextField()
    votes = models.SmallIntegerField(default=0)


class Plan(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=2048)
    created = models.DateTimeField(auto_now_add=True)
