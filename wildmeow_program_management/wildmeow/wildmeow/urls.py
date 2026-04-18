from django.contrib import admin
from django.urls import path, include
from program_management import views as pm_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Root URL → index.html (Program Management index)
    path('', pm_views.index, name='home'),
    # Program Management App URLs
    path('program_management/', include('program_management.urls')),
]
