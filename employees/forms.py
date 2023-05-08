from django import forms 
from .models import Employee


class EmployeeForm(forms.ModelForm):
  class Meta:
    model = Employee
    fields = [ 'first_name', 'last_name','employee_number', 'email', 'department', 'professional_exp']
    labels = {
       
      'first_name': 'First Name', 
      'last_name': 'Last Name', 
      'employee_number': 'Employee Number',
      'email': 'Email', 
      'department': 'Department', 
      'professional_exp': 'Professional Experience(Yrs)'
    }
    widgets = {
      
      'first_name': forms.TextInput(attrs={'class': 'form-control-lg'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control-lg'}),
      'employee_number': forms.NumberInput(attrs={'class': 'form-control-lg'}), 
      'email': forms.EmailInput(attrs={'class': 'form-control-lg'}),
      'department': forms.TextInput(attrs={'class': 'form-control-lg'}),
      'professional_exp': forms.NumberInput(attrs={'class': 'form-control-lg'}),
    }