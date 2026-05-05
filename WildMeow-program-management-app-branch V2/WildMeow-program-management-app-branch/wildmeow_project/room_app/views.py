from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Room, Department

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
    return render(request, 'login.html')

def index(request):
    rooms = Room.objects.all()
    departments = Department.objects.all()
    return render(request, 'index.html', {'rooms': rooms, 'departments': departments})
