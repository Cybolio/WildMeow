from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import DepartmentForm, RegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'management/login.html')

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Registration successful. You can now login.")
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'management/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    return render(request, 'management/index.html')

@login_required(login_url='login')
def edit_profile(request):
    return render(request, 'management/edit_profile.html')

@login_required(login_url='login')
def add_record(request):
    return render(request, 'management/add_record.html')

@login_required(login_url='login')
def add_department(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'management/addNewDepartment.html', {'form': form})
