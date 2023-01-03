from django.shortcuts import render
from .util import recipe_factory as rf
from recipes.models import Recipe


def home(request):
    recipe = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request , 'recipes/pages/home.html', context={
        'recipes': recipe, 
    })


def recipes(request,id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': [rf.make_recipe()],
        'is_detail_page':True
    })

def category(request, category_id):
    recipe = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')
    return render(request , 'recipes/pages/category.html', context={
<<<<<<< HEAD
=======
        'recipes': recipe, 
    })

def author(request, author_id):
    recipe = Recipe.objects.filter(author__id=author_id, is_published=True).order_by('-id')
    return render(request , 'recipes/pages/author.html', context={
>>>>>>> 3a42440f7c362dea72fc2b504d7e74d0fbd2a080
        'recipes': recipe, 
    })

