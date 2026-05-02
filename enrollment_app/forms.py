from django import forms
from .models import User, Payment, Waitlist

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'


class WaitlistForm(forms.ModelForm):
    class Meta:
        model = Waitlist
        fields = '__all__'