from django.urls import path
from recipes import views

#app name serve para referenciar dinamicamente nos links fica 'app_name:name' a view pode mudar mas o name permanece
app_name='recipes'
urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:id>/', views.recipes, name='recipe'),
    path('recipes/category/<int:category_id>/', views.category, name='category'),
]