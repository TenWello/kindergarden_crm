from django.urls import path
from . import views

urlpatterns = [
    path('import-products/', views.import_products_to_inventory, name='import_products_to_inventory'),
    path('', views.inventory_list, name='inventory_list'),
    path('inventory/<int:inventory_id>/ingredients/',
         views.ingredient_list,
         name='ingredient_list'),
    path('add/<int:product_id>/', views.inventory_add_product, name='inventory_add_product'),
    # path('add/', views.inventory_add, name='inventory_add'),
    path('edit/<int:pk>/', views.inventory_edit, name='inventory_edit'),
    path('delete/<int:pk>/', views.inventory_delete, name='inventory_delete'),
    # path('', views.ingredient_list, name='inv_ingredient_list'),
]
