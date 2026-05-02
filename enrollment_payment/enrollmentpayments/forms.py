from django import forms
from .models import User, Payment, Waitlist

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'full_name', 'password', 'role', 'phone_no', 'email_address',]
        widgets = {
            'password': forms.PasswordInput(),
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['student', 'payment_date', 'payment_option']
        widgets = {
            'payment_date': forms.DateInput(attrs={'type': 'date'}),
        }

class WaitlistForm(forms.ModelForm):
    class Meta:
        model = Waitlist
        fields = ['user', 'request_date',]
        widgets = {
            'request_date': forms.DateInput(attrs={'type': 'date'}),
        }