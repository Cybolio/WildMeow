from django import forms
from .models import Grade
from django.contrib.auth.models import User

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]