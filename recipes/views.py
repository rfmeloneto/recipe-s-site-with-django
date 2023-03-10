from django.shortcuts import render
from .util import recipe_factory as rf
from recipes.models import Recipe
from django.http import Http404


def home(request):
    recipe = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request , 'recipes/pages/home.html', context={
        'recipes': recipe, 
    })


def recipes(request,id):
    recipe = Recipe.objects.filter(id = id)
    if not recipe:
        raise Http404('Página Não Existe')
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page':True,
        'title': f'{Recipe.objects.get(id=id).title}',
    })

def category(request, category_id):
    recipe = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')
    if not recipe:
        raise Http404('Página Não Existe')
    return render(request , 'recipes/pages/category.html', context={
        'recipes': recipe, 
        'title': f'{Recipe.objects.first().category.name} | Category'
    })

def author(request, author_id):
    recipe = Recipe.objects.filter(author__id = author_id)
    if not recipe:
        raise Http404('Página Não Existe')
    return render(request, 'recipes/pages/author.html', context={
        'recipes' : recipe,
        'title' : f'{Recipe.objects.first().author.first_name} | author'
    })

