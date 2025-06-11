# ingredient/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ingredient_list, name='ingredient_list'),
    path('add/', views.ingredient_add, name='ingredient_add'),
    path('edit/<int:pk>/', views.ingredient_edit, name='ingredient_edit'),
    path('delete/<int:pk>/', views.ingredient_delete, name='ingredient_delete'),
]
