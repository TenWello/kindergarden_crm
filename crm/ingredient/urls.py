from django.urls import path
from . import views

urlpatterns = [
    path('', views.ingredient_list, name='ingredient_list'),
    path('create/', views.ingredient_create, name='ingredient_create'),
    path('update/<int:pk>/', views.ingredient_update, name='ingredient_update'),
    path('delete/<int:pk>/', views.ingredient_delete, name='ingredient_delete'),
]
