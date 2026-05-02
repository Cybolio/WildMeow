from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),

    path('home/', views.home, name='home'),

    path('grades/add/', views.add_grade, name='add_grade'),

    path('profile/edit/', views.edit_profile, name='edit_profile'),

    path('logout/', views.logout_view, name='logout'),
]