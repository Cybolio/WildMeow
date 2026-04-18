from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),


    path('grades-and-reports/add/', views.add_grade, name='add_grade'),
]