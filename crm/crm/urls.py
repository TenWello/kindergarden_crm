from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from main.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
path('products/', include('product.urls')),
path('payments/', include('payment.urls')),
path('category/', include('category.urls')),
    path('meals/', include('meal.urls')),
    path('ingredients/', include('ingredient.urls')),
    path('inventory/', include('inventory.urls')),
    path('service/', include(('service.urls', 'service'), namespace='service')),
    path('forbidden/', lambda request: render(request, 'forbidden.html'), name='forbidden'),
path('', include('user.urls')),
]
