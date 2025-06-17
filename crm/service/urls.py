from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    path('',               views.service_list,      name='service_list'),
    path('serve/',         views.serve_meal,        name='serve_meal'),
    path('recent/',        views.recent_services,   name='recent_services'),
    path('<int:pk>/',      views.service_detail,    name='service_detail'),
    path('<int:pk>/delete/', views.service_delete,  name='service_delete'),
]
