from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
import json
from .models import User, Employee, Department, Position, LeaveRequest
from .forms.user_forms import UserForm
from .forms.employee_forms import EmployeeForm
from .forms.leave_forms import LeaveRequestForm
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


def employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, 'employee.html', {'employee': employee})


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


def add_leave(request):
    if request.method == 'POST':
        leave_request_form = LeaveRequestForm(request)

        if leave_request_form.is_valid():
            leave_request_form.save()
            return render('employees')
        else:
            return render(request, 'add_leave.html', {
                'leave_request_form': leave_request_form,
                'leave_request_form_errors': json.dumps(leave_request_form.errors)
            })
    else:
        leave_request_form = LeaveRequestForm()
    return render(request, 'add_leave.html', {
        'leave_request_form': leave_request_form
    })
