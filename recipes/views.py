from django.shortcuts import render
from .util import recipe_factory as rf
from recipes.models import Recipe


def home(request):
    recipe = Recipe.objects.all().order_by('-id')
    return render(request , 'recipes/pages/home.html', context={
        'recipes': recipe, 
    })


def recipes(request,id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': [rf.make_recipe()],
        'is_detail_page':True
    })

def category(request, category_id):
    recipe = Recipe.objects.filter(category__id=category_id).order_by('-id')
    return render(request , 'recipes/pages/home.html', context={
        'recipes': recipe, 
    })