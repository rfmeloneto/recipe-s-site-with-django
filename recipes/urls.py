from django.urls import path
from recipes.views import home, base

urlpatterns = [
    path('',home),
    path('base/', base),
]