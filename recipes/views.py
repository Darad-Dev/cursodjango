from django.shortcuts import render


def sobre(request):
    return render(request, "recipes/sobre.html", context={'name': 'Fabio Dev'})

def home(request):
    return render(request, 'recipes/home.html')

def contact(request):
    return render(request, 'recipes/contact.html')
