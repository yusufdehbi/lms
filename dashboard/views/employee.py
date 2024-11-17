from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
import json
from dashboard.models import User, Employee, Position
from dashboard.forms.user_forms import UserForm
from dashboard.forms.employee_forms import EmployeeForm
from django.core.paginator import Paginator


# @role_required(allowed_roles=[User.ROLE_EXECUTIVE_MANAGER, User.ROLE_DEPARTMENT_MANAGER, User.ROLE_HR_MANAGER])
def employees(request):
    employees = Employee.objects.all()
    paginator = Paginator(employees, 10)
    page_number = request.GET.get('page')
    page_employees = paginator.get_page(page_number)
    return render(request, 'pages/employee/employees.html', {'employees': page_employees})


def employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, 'pages/employee/employee.html', {'employee': employee})


def add_employee(request):
    positions = Position.objects.all()
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
            return render(request, 'pages/employee/add_employee.html', {
                'user_form': user_form,
                'employee_form': employee_form,
                'user_form_errors': json.dumps(user_form.errors),
                'employee_form_errors': json.dumps(employee_form.errors),
                'positions': positions
            })

    else:
        user_form = UserForm()
        employee_form = EmployeeForm()
    return render(request, 'pages/employee/add_employee.html', {
        'user_form': user_form,
        'employee_form': employee_form,
        'positions': positions
    })

