from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import UserForm, PaymentForm, WaitlistForm

def index(request):
    return render(request, 'index.html')

def addNewUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'addNewUser.html', {'form': form})

def addNewPayment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PaymentForm()
    return render(request, 'addNewPayment.html', {'form': form})

def addNewWaitlist(request):
    if request.method == 'POST':
        form = WaitlistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = WaitlistForm()
    return render(request, 'addNewWaitlist.html', {'form': form})