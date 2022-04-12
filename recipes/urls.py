from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe), #'recipe' é a view e 'recipes' é o url que quero mostrar no browser

]