
from django.shortcuts import render, redirect
from .forms import DepartmentForm

def index(request):
    return render(request, 'management/index.html')

def add_department(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'management/addNewDepartment.html', {'form': form})
