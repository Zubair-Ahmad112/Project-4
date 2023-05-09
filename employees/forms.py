from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(
        attrs={'class': 'form-control-sm'}))

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'employee_number',
                  'email', 'department', 'professional_exp', 'gender']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'employee_number': 'Employee Number',
            'email': 'Email',
            'department': 'Department',
            'professional_exp': 'Professional Experience(Yrs)',
            'gender': 'Gender'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'employee_number': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'email': forms.EmailInput(attrs={'class': 'form-control-sm'}),
            'department': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'professional_exp': forms.NumberInput(attrs={'class': 'form-control-sm'}),
        }
