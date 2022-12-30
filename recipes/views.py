from django.shortcuts import render
from .util import recipe_factory as rf


def home(request):
    return render(request , 'recipes/pages/home.html', context={
        'recipes':[rf.make_recipe() for _ in range(10)]
    })


def recipes(request,id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': [rf.make_recipe()]
    })