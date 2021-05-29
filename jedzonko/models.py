from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=256)
    ingredients = models.TextField(max_length=1024)
    description = models.TextField(max_length=2048)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    preparation_time = models.PositiveSmallIntegerField()
    way_of_preparing = models.TextField()
    votes = models.SmallIntegerField(default=0, null=True)


class Plan(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=2048)
    created = models.DateTimeField(auto_now_add=True)
    recipes = models.ManyToManyField(Recipe, through="RecipePlan")


class Dayname(models.Model):
    day_name = models.CharField(max_length=16)
    order = models.IntegerField(default=0, unique=True)


class RecipePlan(models.Model):
    meal_name = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    order = models.IntegerField(default=0, unique=True)
    day_name = models.ManyToManyField(Dayname)
