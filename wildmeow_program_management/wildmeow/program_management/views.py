from django.shortcuts import render, redirect
from .models import Program, Semester
from .forms import ProgramForm, SemesterForm


def index(request):
    programs = Program.objects.all()
    semesters = Semester.objects.all()
    context = {
        'programs': programs,
        'semesters': semesters,
    }
    return render(request, 'program_management/index.html', context)


def addNewProgram(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('program_management:index')
    else:
        form = ProgramForm()
    return render(request, 'program_management/addNewProgram.html', {'form': form})


def addNewSemester(request):
    if request.method == 'POST':
        form = SemesterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('program_management:index')
    else:
        form = SemesterForm()
    return render(request, 'program_management/addNewSemester.html', {'form': form})
