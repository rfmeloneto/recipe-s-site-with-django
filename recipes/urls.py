from django.urls import path
from recipes.views import home, recipes

urlpatterns = [
    path('',home),
    path('recipes/', recipes)
    
]