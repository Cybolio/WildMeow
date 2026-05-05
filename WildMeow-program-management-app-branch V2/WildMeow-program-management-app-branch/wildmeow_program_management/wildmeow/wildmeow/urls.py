from django.contrib import admin
from django.urls import path, include
from program_management import views as pm_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Root URL → login page
    path('', pm_views.login_view, name='home'),
    # Program Management App
    path('program_management/', include('program_management.urls')),
]
