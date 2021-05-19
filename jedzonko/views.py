import random
from datetime import datetime
from django.http import HttpResponse

from django.shortcuts import render
from django.views import View
from jedzonko.models import Recipe


class IndexView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "test.html", ctx)


class RecipeListView(View):

    def get(self, request):
        return render(request, "app-recipes.html")

      
def index_site(request):
    recipes = Recipe.objects.all()
    list_recipes = list(recipes)
    random.shuffle(list_recipes)
    random_3_recipes = list_recipes[:3]
    return render(request, template_name="index.html", context={'random_3_recipes': random_3_recipes})
