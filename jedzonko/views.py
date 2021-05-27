from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class IndexView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "test.html", ctx)


class RecipeListView(View):

    def get(self, request):
        return render(request, "app-recipes.html")

    
def index_site(request):
    return render(request, "index.html")


class DashboardView(View):
    def get(self,request):
        return render(request, "dashboard.html")

class RecipeListView(View):
    def get(self,request):
        return render(request, 'app-recipes.html')

class RecipeAddView(View):
    def get(self,request):
        return render(request, 'app-add-recipe.html')

class RecipeModifyView(View):
    def get(self,request,id):
        return HttpResponse(f"Działa id:{id}")

class RecipeDetails(View):
    def get(self,request, id):
        return render(request, app-recipe-details.html)

class PlanIdView(View):
    def get(self,request,id):
        return HttpResponse(f"Działa id: {id}")

class PlanAddView(View):
    def get(self,request):
        return HttpResponse("Dodajmy nowy plan")

class PlanAddReceipeView(View):
    def get(self, request):
        return HttpResponse("Dodajmy nowy przepis do planu")

class PlanListView(View):
    def get(self,request):
        return render(request, 'app-schedules.html')

class PlanListView(View):
    def get(self, request):
        return HttpResponse('lista planów')