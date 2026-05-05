
from django.urls import path
from . import views

urlpatterns = [
    path('addDepartment', views.add_department, name='add_department'),
]
