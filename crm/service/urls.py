from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_list, name='service_list'),
    path('serve/', views.serve_meal, name='serve_meal'),
    path('recent/', views.recent_services, name='recent_services'),
]
