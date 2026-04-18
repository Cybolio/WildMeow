from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Room, Department
from django.contrib import messages

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
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    rooms = Room.objects.all()
    departments = Department.objects.all()
    return render(request, 'index.html', {'rooms': rooms, 'departments': departments})

@login_required(login_url='login')
def edit_profile(request):
    # Placeholder for edit profile
    return render(request, 'edit_profile.html')

@login_required(login_url='login')
def add_record(request):
    # Placeholder for add new record
    return render(request, 'add_record.html')
