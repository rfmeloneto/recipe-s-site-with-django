from django.shortcuts import render

def home(request):
    return render(request , 'recipes/home.html')

def base(request):
    return render(request, 'global/home.html')
