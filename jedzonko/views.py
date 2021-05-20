from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
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
    return render(request, "index.html")



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

