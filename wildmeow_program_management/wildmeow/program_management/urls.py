from django.urls import path
from . import views

app_name = 'program_management'

urlpatterns = [
    path('', views.index, name='index'),
    path('addNewProgram/', views.addNewProgram, name='addNewProgram'),
    path('addNewSemester/', views.addNewSemester, name='addNewSemester'),
]

# URL patterns accessible at:
# 127.0.0.1:8000/                            → index.html
# 127.0.0.1:8000/program_management/addNewProgram/  → Add New Program form
# 127.0.0.1:8000/program_management/addNewSemester/ → Add New Semester form
