from django.contrib import admin
from recipes.models import Category, Recipe


#cria as classes para aparecer no painel de admins
class CategoryAdmin(admin.ModelAdmin):
    pass

#usando o decorator para fazer aparecer no admind
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass
#usando uma função para aparecer no admin (nome do model, nome da classe no admin.py)
admin.site.register(Category, CategoryAdmin)
