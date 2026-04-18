from django.shortcuts import render, redirect
from .models import Grade
from .forms import GradeForm

def index(request):
    grades = Grade.objects.all()
    return render(request, 'index.html', {'grades': grades})

def add_grade(request):
    form = GradeForm()

    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'addNewGrade.html', {'form': form})