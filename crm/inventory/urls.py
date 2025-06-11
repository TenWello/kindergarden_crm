from django.urls import path
from . import views

urlpatterns = [
    path('import-products/', views.import_products_to_inventory, name='import_products_to_inventory'),
path('', views.inventory_list, name='inventory_list'),
    # Yangi product uchun inventory kiritish
    path('add/<int:product_id>/', views.inventory_add_product, name='inventory_add_product'),
    # path('add/', views.inventory_add, name='inventory_add'),
    path('edit/<int:pk>/', views.inventory_edit, name='inventory_edit'),
    path('delete/<int:pk>/', views.inventory_delete, name='inventory_delete'),
]
