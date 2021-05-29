import random
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from jedzonko.models import *


class IndexView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "test.html", ctx)


class RecipeListView(ListView):

    model = Recipe
    template_name = 'app-recipes.html'
    context_object_name = 'recipes'
    paginate_by = 50

    def get_queryset(self, *args, **kwargs):
        return Recipe.objects.all().order_by('-votes', '-created')


def index_site(request):
    recipes = Recipe.objects.all()
    list_recipes = list(recipes)
    random.shuffle(list_recipes)
    random_3_recipes = list_recipes[:3]
    return render(request, template_name="index.html", context={'random_3_recipes': random_3_recipes})


class RecipeAddView(View):

    def get(self, request):
        return render(request, 'app-add-recipe.html')


    def post(self,request):
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')
        time_of_preparing = request.POST.get('time_of_preparing')
        way_of_preparing = request.POST.get('way_of_preparing')
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
        return render(request, 'app-add-schedules.html')
    def post(self, request):
        planName = request.POST.get('planName')
        planDescription = request.POST.get('planDescription')
        return HttpResponse(f'{planName}, {planDescription}')


class RecipeListView(View):
    def get(self,request):
        return render(request, 'app-recipes.html')

class RecipeAddView(View):
    def get(self,request):
        return render(request, 'app-add-recipe.html')

class RecipeModifyView(View):
    def get(self,request,id):
        return HttpResponse(f"Działa id:{id}")

class PlanAddReceipeView(View):
    def get(self, request):
        plans = Plan.objects.all()
        recipes = Recipe.objects.all()
        days = Dayname.objects.all()
        ctx = {
            'plans': plans,
            'recipes': recipes,
            'days': days,
        }
        return render(request, template_name='app-schedules-meal-recipe.html', context=ctx)
    def post(self, request, *args, **kwargs):
        plan_id = request.POST.get('choosePlan')
        recipe_id = request.POST.get('recipie')
        day_name_id = request.POST.get('day')
        order = request.POST.get('number')
        meal_name = request.POST.get('name')
        if all([plan_id, recipe_id, day_name_id, order, meal_name]):
            RecipePlan.objects.create(meal_name=meal_name, order=order,
                                     day_name_id=day_name_id, recipe_id=recipe_id, plan_id=plan_id)
            return redirect(f'/plan/{plan_id}')
        else:
            message = 'Proszę wypełnić wszystkie pola'
        return render(request, template_name='app-schedules-meal-recipe.html', context={'message': message})


class PlanListView(ListView):

    model = Plan
    template_name = 'app-schedules.html'
    context_object_name = 'plans'
    paginate_by = 50

    def get_queryset(self, *args, **kwargs):
        return Plan.objects.all().order_by('name')
      


class DashboardView(View):

    def get(self, request, *args, **kwargs):
        plans = Plan.objects.count()
        recipes = Recipe.objects.count()
        ctx = {
            'plans': plans,
            'recipes': recipes,
        }
        return render(request, "dashboard.html", context=ctx)


class RecipeDetails(View):
    def get(self, request, id):
        recipe = Recipe.objects.get(id=id)
        ingredients = recipe.ingredients.split(sep=', ')
        ctx = {
            'recipe': recipe,
            'ingredients': ingredients,
        }
        return render(request, template_name='app-recipe-details.html', context=ctx)

class ReceipeIdView(View):
    def get(self,request,id):
        recipe = Recipe.objects.get(id=id)
        return render(request, 'recipe-id-vote.html',context = {'id':recipe})

    def post(self,request,id):

        recipe = Recipe.objects.get(id=id)
        nr_voices = recipe.votes
        new_nr_voices = nr_voices + 1
        recipe.votes = new_nr_voices
        recipe.save()

        return HttpResponseRedirect(f'/recipe/{id}')

