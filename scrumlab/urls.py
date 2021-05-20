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
from jedzonko.views import (index_site, dashboard, IndexView, RecipeListView, ReceipeAddView,RecipeModifyView,PlanIdView,
                            PlanAddView,PlanAddReceipeView,PlanListView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', IndexView.as_view()),
    path('', index_site),
    path('main/', dashboard),
    path('recipe/list/', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/add/', ReceipeAddView.as_view(), name='receipe-add'),
    path('recipe/modify/<int:id>', RecipeModifyView.as_view(), name='recipe-modify'),
    path('plan/<int:id>', PlanIdView.as_view(), name='plan-id'),
    path('plan/add/', PlanAddView.as_view(), name='plan-add'),
    path('plan/add-recipe/', PlanAddReceipeView.as_view(), name='plan-add-receipe'),
    path('plan/list/', PlanListView.as_view(), name='plan-list'),

]
