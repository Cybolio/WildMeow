from django.shortcuts import render, redirect
from .models import User, Payment, Waitlist
from .forms import UserForm, PaymentForm, WaitlistForm



def login_view(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username, password=password)
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            return redirect('/home')
        except User.DoesNotExist:
            error = 'Invalid username or password.'
    return render(request, 'login.html', {'error': error})



def home_view(request):
    if not request.session.get('user_id'):
        return redirect('/')
    return render(request, 'index.html', {'username': request.session.get('username')})



def edit_profile_view(request):
    if not request.session.get('user_id'):
        return redirect('/')
    user = User.objects.get(id=request.session.get('user_id'))
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            request.session['username'] = user.username
            return redirect('/home')
    else:
        form = UserForm(instance=user)
    return render(request, 'editProfile.html', {'form': form})



def logoff_view(request):
    request.session.flush()
    return redirect('/')



def add_new_user(request):
    if not request.session.get('user_id'):
        return redirect('/')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = UserForm()
    return render(request, 'addNewUser.html', {'form': form})


def add_new_payment(request):
    if not request.session.get('user_id'):
        return redirect('/')
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = PaymentForm()
    return render(request, 'addNewPayment.html', {'form': form})


def add_new_waitlist(request):
    if not request.session.get('user_id'):
        return redirect('/')
    if request.method == 'POST':
        form = WaitlistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = WaitlistForm()
    return render(request, 'addNewWaitlist.html', {'form': form})