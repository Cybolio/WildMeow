from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Program, Semester
from .forms import ProgramForm, SemesterForm, EditProfileForm


# ─── LOGIN ───────────────────────────────────────────────────────────────────

def login_view(request):
    # If already logged in, go straight to home
    if request.user.is_authenticated:
        return redirect('program_management:index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name or user.username}!')
            return redirect('program_management:index')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'program_management/login.html')


# ─── LOGOUT ──────────────────────────────────────────────────────────────────

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('program_management:login')


# ─── INDEX (Home) ─────────────────────────────────────────────────────────────

@login_required(login_url='program_management:login')
def index(request):
    programs = Program.objects.all()
    semesters = Semester.objects.all()
    context = {
        'programs': programs,
        'semesters': semesters,
        'user': request.user,
    }
    return render(request, 'program_management/index.html', context)


# ─── EDIT PROFILE ─────────────────────────────────────────────────────────────

@login_required(login_url='program_management:login')
def edit_profile(request):
    user = request.user

    if request.method == 'POST':
        form = EditProfileForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            new_password = form.cleaned_data['new_password']
            if new_password:
                user.set_password(new_password)
                messages.warning(request, 'Password changed. Please log in again.')
                user.save()
                logout(request)
                return redirect('program_management:login')
            user.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('program_management:index')
    else:
        form = EditProfileForm(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        })

    return render(request, 'program_management/edit_profile.html', {'form': form, 'user': user})


# ─── ADD NEW PROGRAM ──────────────────────────────────────────────────────────

@login_required(login_url='program_management:login')
def addNewProgram(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New program added successfully!')
            return redirect('program_management:index')
    else:
        form = ProgramForm()
    return render(request, 'program_management/addNewProgram.html', {'form': form})


# ─── ADD NEW SEMESTER ─────────────────────────────────────────────────────────

@login_required(login_url='program_management:login')
def addNewSemester(request):
    if request.method == 'POST':
        form = SemesterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New semester added successfully!')
            return redirect('program_management:index')
    else:
        form = SemesterForm()
    return render(request, 'program_management/addNewSemester.html', {'form': form})
