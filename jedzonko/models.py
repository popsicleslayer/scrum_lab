from django.db import models


# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=256)
    ingredients = models.TextField(max_length=1024)
    description = models.TextField(max_length=2048)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    preparation_time = models.PositiveSmallIntegerField()
    votes = models.SmallIntegerField(default=0)
    preparation = models.TextField(max_length=2048)


class Plan(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=2048)
    created = models.DateTimeField(auto_now_add=True)


class Page(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.CharField(max_length=256, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(" ", "_").lower()
        super().save(*args, **kwargs)
