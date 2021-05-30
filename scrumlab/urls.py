"""scrumlab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from jedzonko.views import (index_site, DashboardView, IndexView, RecipeListView, RecipeAddView,RecipeModifyView,PlanIdView,
                            PlanAddView,PlanAddReceipeView,PlanListView,ReceipeIdView,RecipeDetails)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', IndexView.as_view()),
    path('', index_site),
    path('main/', DashboardView.as_view()),
    path('recipe/list/', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/add/', RecipeAddView.as_view(), name='recipe-add'),
    path('recipe/modify/<int:id>', RecipeModifyView.as_view(), name='recipe-modify'),
    path('recipe/<int:id>/', RecipeDetails.as_view()),
    path('plan/<int:id>', PlanIdView.as_view(), name='plan-id'),
    path('plan/add/', PlanAddView.as_view(), name='plan-add'),
    path('plan/add-recipe/', PlanAddReceipeView.as_view(), name='plan-add-recipe'),
    path('plan/list/', PlanListView.as_view(), name='plan-list'),
    path('recipe/<int:id>', ReceipeIdView.as_view(), name='recipe-id')

]
