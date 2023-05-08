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
 
    

