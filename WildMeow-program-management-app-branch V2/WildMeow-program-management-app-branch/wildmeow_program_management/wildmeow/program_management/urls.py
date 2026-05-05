from django.urls import path
from . import views

app_name = 'program_management'

urlpatterns = [
    # Auth
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),

    # Home / Index
    path('', views.index, name='index'),

    # Records
    path('addNewProgram/', views.addNewProgram, name='addNewProgram'),
    path('addNewSemester/', views.addNewSemester, name='addNewSemester'),
]

# URL Summary:
# 127.0.0.1:8000/                                   → login page (redirects to index if logged in)
# 127.0.0.1:8000/program_management/login/          → login page
# 127.0.0.1:8000/program_management/logout/         → logs out, redirects to login
# 127.0.0.1:8000/program_management/edit-profile/   → edit profile page
# 127.0.0.1:8000/program_management/addNewProgram/  → add new program
# 127.0.0.1:8000/program_management/addNewSemester/ → add new semester
