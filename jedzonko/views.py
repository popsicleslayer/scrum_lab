import random
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
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
        time_of_preparing = request.POST.get('preparation_time')
        ingredients = request.POST.get('ingredients')
        way_of_preparing = request.POST.get('way_of_preparing')
        if all([recipe_name, ingredients, recipe_description, time_of_preparing, way_of_preparing]):
            Recipe.objects.create(name=recipe_name, ingredients=ingredients, description=recipe_description,
                                  preparation_time=time_of_preparing, way_of_preparing=way_of_preparing)
            return redirect('/recipe/list/')
        else:
            message = "Wypełnij poprawnie wszystkie pola."
        return render(request, "app-add-recipe.html", {"message": message})


class RecipeModifyView(View):
    def get(self, reqest, id):
        return HttpResponse(f"Działa id:{id}")


class PlanIdView(View):
    def get(self, request, id):
        plan = Plan.objects.get(pk=id)
        recipePlan = RecipePlan.objects.filter(plan=plan.id)
        return render(request,template_name='app-details-schedules.html', context={'plan': plan, 'recipePlan': recipePlan})


class PlanAddView(View):

    def get(self,request):
        return render(request, 'app-add-schedules.html')
    def post(self, request):
        planName = request.POST.get('planName')
        planDescription = request.POST.get('planDescription')
        if all([planName, planDescription]):
            new = Plan.objects.create(name=planName, description=planDescription)
            new.save()
        else:
            return HttpResponse("Wprowadzono niepełne dane")

        response = redirect(f'/plan/{new.id}/details')
        return response

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
        plan_id = request.POST.get('choose_plan')
        recipe_id = request.POST.get('recipe')
        day_name_id = request.POST.get('day_name')
        order = request.POST.get('order')
        meal_name = request.POST.get('meal_name')
        recipe = Recipe.objects.get(pk=recipe_id)
        plan = Plan.objects.get(pk=plan_id)
        day_name = Dayname.objects.get(pk=day_name_id)
        if all([plan_id, recipe_id, day_name_id, order, meal_name]):
            object = RecipePlan.objects.create(meal_name=meal_name, order=order, recipe=recipe, plan=plan)
            object.save()
            object.day_name.add(day_name)
            return redirect(f'/plan/{plan_id}')
        else:
            message = 'Proszę wypełnić wszystkie pola'
            plans = Plan.objects.all()
            recipes = Recipe.objects.all()
            days = Dayname.objects.all()
            ctx = {
                'plans': plans,
                'recipes': recipes,
                'days': days,
                'message': message,
            }
        return render(request, template_name='app-schedules-meal-recipe.html', context=ctx)


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


class RecipeModifyView(View):
    def get(self, request, id):
        recipe = get_object_or_404(Recipe, pk=id)
        name = recipe.name
        ingredients = recipe.ingredients
        description = recipe.description
        preparation_time = recipe.preparation_time
        way_of_preparing = recipe.way_of_preparing
        ctx = {"name": name,
               "recipe_id": id,
               "ingredients": ingredients,
               "description": description,
               "preparation_time": preparation_time,
               "way_of_preparing": way_of_preparing}
        return render(request, "app-edit-recipe.html", ctx)

    def post(self, request, id):
        recipe = Recipe.objects.filter(pk=id)
        name = request.POST.get('name')
        ingredients = request.POST.get('ingredients')
        description = request.POST.get('description')
        preparation_time = request.POST.get('preparation_time')
        way_of_preparing = request.POST.get('way_of_preparing')
        if all([name, ingredients, description, preparation_time, way_of_preparing]):
            recipe.update(name=name, ingredients=ingredients, description=description,
                          preparation_time=preparation_time, way_of_preparing=way_of_preparing)
            return redirect('/recipe/list/')
        else:
            message = "Wypełnij poprawnie wszystkie pola."
        return render(request, "app-edit-recipe.html", {"message": message})


class ReceipeIdView(View):
    def get(self,request,id):
        recipe = Recipe.objects.get(id=id)
        return render(request, 'recipe-id-vote.html',context = {'id':recipe})

    def post(self,request,id):

        recipe = Recipe.objects.get(id=id)
        nr_voices = recipe.votes
        if 'like' in request.POST:
            new_nr_voices = nr_voices + 1
            recipe.votes = new_nr_voices
            recipe.save()
        elif 'dislike':
            new_nr_voices = nr_voices - 1
            recipe.votes = new_nr_voices
            recipe.save()
        return HttpResponseRedirect(f'/recipe/{id}')


class ContactDetailsView(View):
    def get(self, request, *args, **kwargs):
        try:
            contact_details = Page.objects.get(slug='contact')
        except Page.DoesNotExist:
            return redirect('/#contact')
        context = {'paragraph': contact_details.description}
        return render(request, 'contact-details.html', context)





