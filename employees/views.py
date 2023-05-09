from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse

from .models import Employee
from .forms import EmployeeForm





# Creating views below


def main(request):
  

  return render(request, 'employees/index.html', {
  'employees': Employee.objects.all()})
 
    

def view(request, id):
  return HttpResponseRedirect(reverse('index'))

def info(request):
  return render(request,'employees/info.html')

def adding(request):
  if request.method == 'POST':
    form = EmployeeForm(request.POST)
    if form.is_valid():
      
      new_first_name = form.cleaned_data['first_name']
      new_last_name = form.cleaned_data['last_name']
      new_employee_number = form.cleaned_data['employee_number']
      new_email = form.cleaned_data['email']
      new_department = form.cleaned_data['department']
      new_professional_exp = form.cleaned_data['professional_exp']
      new_gender = form.cleaned_data['gender']

      new_employee = Employee(
        
        first_name = new_first_name,
        last_name = new_last_name,
        employee_number = new_employee_number,
        email = new_email,
        department = new_department,
        professional_exp = new_professional_exp,
        gender = new_gender
      )
      new_employee.save()
      return render(request, 'employees/add.html', {
        'form': EmployeeForm(),
        'success': True
      })
  else:
    form = EmployeeForm()
  return render(request, 'employees/add.html', {
    'form': EmployeeForm()
  })

def update(request, id):
  if request.method == 'POST':
    employee = Employee.objects.get(pk=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
      form.save()
      return render(request, 'employees/edit.html', {
        'form': form,
        'success': True
      })
  else:
    employee = Employee.objects.get(pk=id)
    form = EmployeeForm(instance=employee)
  return render(request, 'employees/edit.html', {
    'form': form
  })

def destroy(request, id):
  if request.method == 'POST':
    employee = Employee.objects.get(pk=id)
    employee.delete()
  return HttpResponseRedirect(reverse('index'))




