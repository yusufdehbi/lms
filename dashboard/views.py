from django.shortcuts import render, redirect
from django.db import transaction
import json
from .models import User, Employee, Department, Position
from .forms.user_forms import UserForm
from .forms.employee_forms import EmployeeForm
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    return render(request, 'overview.html')


def employees(request):
    employees = Employee.objects.all()
    paginator = Paginator(employees, 10)
    page_number = request.GET.get('page')
    page_employees = paginator.get_page(page_number)
    return render(request, 'employees.html', {'employees': page_employees})


def add_employee(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        employee_form = EmployeeForm(request.POST)

        if user_form.is_valid() and employee_form.is_valid():
            with transaction.atomic():
                user = user_form.save(commit=False)
                user.role = User.ROLE_EMPLOYEE
                user.save()

                employee = employee_form.save(commit=False)
                employee.user = user
                employee.save()

            return redirect('employees')
        else:
            return render(request, 'add_employee.html', {
                'user_form': user_form,
                'employee_form': employee_form,
                'user_form_errors': json.dumps(user_form.errors),
                'employee_form_errors': json.dumps(employee_form.errors),
            })

    else:
        user_form = UserForm()
        employee_form = EmployeeForm()
    return render(request, 'add_employee.html', {
        'user_form': user_form,
        'employee_form': employee_form,
    })
