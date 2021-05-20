from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from jedzonko.models import Recipe


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
    return render(request, "index.html")


def dashboard(request):
    return render(request, "dashboard.html")