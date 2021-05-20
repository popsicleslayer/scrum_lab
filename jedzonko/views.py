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
        recipes = Recipe.objects.all().order_by('-votes', '-created')
        ctx = {
            'recipes': recipes,
        }
        return render(request, "app-recipes.html", context=ctx)

    
def index_site(request):
    return render(request, "index.html")


def dashboard(request):
    return render(request, "dashboard.html")