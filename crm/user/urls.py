from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('serve-meal/', views.serve_meal, name='serve_meal'),
    path('inventory-dashboard/', views.inventory_dashboard, name='inventory_dashboard'),
    path('forbidden/', views.forbidden, name='forbidden'),
]
