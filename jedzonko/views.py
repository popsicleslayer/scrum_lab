from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from jedzonko.models import Recipe, Plan


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

    def get(self, request, *args, **kwargs):
        plans = Plan.objects.count()
        ctx = {
            'plans': plans,
        }
        return render(request, "dashboard.html", context=ctx)
