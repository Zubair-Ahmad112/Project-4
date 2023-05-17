from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group


def is_manager(user):
    return user.groups.filter(name='manager').exists()


manager_required = user_passes_test(is_manager, login_url='login')


# Creating views below


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the email and password belong to one of the users in the database
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            # Invalid credentials, show an error message
            messages.error(request, 'Invalid email or password')
            return render(request, 'employees/login.html',)

    return render(request, 'employees/login.html')


@login_required
def main(request):
    return render(request, 'employees/index.html', {
        'employees': Employee.objects.all()})


@login_required
def view(request, id):
    return HttpResponseRedirect(reverse('index'))


@login_required
def info(request):
    return render(request, 'employees/info.html')


@login_required
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

                first_name=new_first_name,
                last_name=new_last_name,
                employee_number=new_employee_number,
                email=new_email,
                department=new_department,
                professional_exp=new_professional_exp,
                gender=new_gender
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


@login_required
@manager_required
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


@login_required
@manager_required
def destroy(request, id):
    if request.method == 'POST':
        employee = Employee.objects.get(pk=id)
        employee.delete()
    return HttpResponseRedirect(reverse('index'))


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
