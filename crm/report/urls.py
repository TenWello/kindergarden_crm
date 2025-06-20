from django.urls import path
from . import views

app_name = 'report'

urlpatterns = [
    path('',                    views.report_list,   name='report_list'),
    path('generate/<int:year>/<int:month>/',
                                 views.generate_report, name='generate_report'),
    path('<int:pk>/',           views.report_detail, name='report_detail'),
    path('<int:pk>/delete/',    views.report_delete, name='report_delete'),
]
