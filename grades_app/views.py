from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Grade
from .forms import GradeForm
from .forms import EditProfileForm


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')


@login_required
def home(request):
    grades = Grade.objects.all()
    return render(request, 'index.html', {'grades': grades})


@login_required
def add_grade(request):
    form = GradeForm()

    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'addNewGrade.html', {'form': form})


@login_required
def edit_profile(request):
    user = request.user

    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditProfileForm(instance=user)

    return render(request, 'edit_profile.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')