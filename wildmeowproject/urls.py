from django.contrib import admin
from django.urls import path, include
from enrollment_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('enrollment_app/', include('enrollment_app.urls')),
]