import random
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
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

class ReceipeAddView(View):
    def get(self,request):
        return render(request, 'app-add-recipe.html')

    def post(self,request):
        recipe_name = request.POST.get('receipe_name')
        recipe_description = request.POST.get('receipe_description')
        time_of_preparing = request.POST.get('time_of_preparing')
        way_of_preparing = request.POST.get('way_of_preparing')
        ingredients = request.POST.get('ingredients')

        Recipe.objects.create(name=recipe_name, description = recipe_description,preparation_time= time_of_preparing, ingredients= ingredients )

        return render(request, "app-add-recipe.html")

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
        ctx = {
            'plans': plans,
        }
        return render(request, "dashboard.html", context=ctx)

