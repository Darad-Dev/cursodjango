from django.contrib import admin
from django.urls import path
from recipes.views import home, sobre, contact


urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contact),
]