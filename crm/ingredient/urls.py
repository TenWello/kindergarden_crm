from django.urls import path
from . import views

urlpatterns = [
    path('', views.ingredient_manage, name='ingredient_manage'),
# path('create/', views.ingredient_create, name='ingredient_create'),
    path('delete/<int:pk>/', views.ingredient_delete, name='ingredient_delete'),
]
