import random
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from jedzonko.models import Recipe
from jedzonko.models import *


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



def dashboard(request):
    return render(request, "dashboard.html")


class RecipeAddView(View):
    def get(self, request):
        return render(request, 'app-add-recipe.html')

    def post(self, request):
        name = request.POST.get('recipe_name')
        ingredients = request.POST.get('ingredients')
        description = request.POST.get('recipe_description')
        preparation_time = request.POST.get('time_of_preparing')
        way_of_preparing = request.POST.get('way_of_preparing')
        if all([name, ingredients, description, preparation_time, way_of_preparing]):
            Recipe.objects.create(name=name, ingredients=ingredients, description=description,
                                  preparation_time=preparation_time, way_of_preparing=way_of_preparing)
            return redirect('/recipe/list/')
        else:
            message = "Wypełnij poprawnie wszystkie pola."
        return render(request, "app-add-recipe.html", {"message": message})


class RecipeModifyView(View):
    def get(self, reqest, id):
        return HttpResponse(f"Działa id:{id}")

class PlanIdView(View):
    def get(self, request, id):
        return HttpResponse(f"Działa id: {id}")

class PlanAddView(View):
    def get(self,request):
        return HttpResponse("Dodajmy nowy plan")

class PlanAddReceipeView(View):
    def get(self, request):
        return HttpResponse("Dodajmy nowy przepis do planu")

class PlanListView(View):
    def get(self,request):
        return HttpResponse("Tutaj będzie lista wszystkich planów")

class DashboardView(View):

    def get(self, request, *args, **kwargs):
        plans = Plan.objects.count()
        ctx = {
            'plans': plans,
        }
        return render(request, "dashboard.html", context=ctx)

