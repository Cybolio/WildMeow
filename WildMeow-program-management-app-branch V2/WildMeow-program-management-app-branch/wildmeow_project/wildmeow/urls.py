
from django.contrib import admin
from django.urls import path, include
from management import views

urlpatterns = [
    path('', views.index, name='index'),
    path('management/', include('management.urls')),
]
