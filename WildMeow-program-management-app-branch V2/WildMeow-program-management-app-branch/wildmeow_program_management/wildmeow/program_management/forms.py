from django import forms
from .models import Program, Semester


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
            'autofocus': True,
        }),
        label='Username'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
        }),
        label='Password'
    )


class EditProfileForm(forms.Form):
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First name',
        }),
        label='First Name'
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last name',
        }),
        label='Last Name'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email address',
        }),
        label='Email'
    )
    new_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Leave blank to keep current password',
        }),
        label='New Password'
    )


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = [
            'Program_Name',
            'Program_Code',
            'Department_ID',
            'Total_Units',
            'Program_Duration',
            'Associated_Courses',
        ]
        widgets = {
            'Program_Name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Bachelor of Science in Computer Science',
            }),
            'Program_Code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. BSCS',
            }),
            'Department_ID': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Department ID',
            }),
            'Total_Units': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 120',
            }),
            'Program_Duration': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Duration in years (e.g. 4)',
            }),
            'Associated_Courses': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'List associated course codes...',
                'rows': 3,
            }),
        }
        labels = {
            'Program_Name': 'Program Name',
            'Program_Code': 'Program Code',
            'Department_ID': 'Department ID',
            'Total_Units': 'Total Units',
            'Program_Duration': 'Program Duration (Years)',
            'Associated_Courses': 'Associated Courses',
        }


class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = [
            'Academic_Year',
            'Term',
            'Start_Date',
            'End_Date',
            'Enrollment_Start',
            'Enrollment_End',
        ]
        widgets = {
            'Academic_Year': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 2024-2025',
            }),
            'Term': forms.Select(attrs={
                'class': 'form-control',
            }),
            'Start_Date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'End_Date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'Enrollment_Start': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'Enrollment_End': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
        }
        labels = {
            'Academic_Year': 'Academic Year',
            'Term': 'Term',
            'Start_Date': 'Start Date',
            'End_Date': 'End Date',
            'Enrollment_Start': 'Enrollment Start',
            'Enrollment_End': 'Enrollment End',
        }
