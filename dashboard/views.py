from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
import json
from dashboard.utils.auth_utils import role_required

from django.views.decorators.csrf import csrf_exempt

from .models import User, Employee, Department, Position, LeaveRequest, LeaveType
from .forms.user_forms import UserForm
from .forms.employee_forms import EmployeeForm
from .forms.leave_forms import LeaveRequestForm
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    return render(request, 'overview.html')


# @role_required(allowed_roles=[User.ROLE_EXECUTIVE_MANAGER, User.ROLE_DEPARTMENT_MANAGER, User.ROLE_HR_MANAGER])
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
            return render(request, 'add_employee.html', {
                'user_form': user_form,
                'employee_form': employee_form,
                'user_form_errors': json.dumps(user_form.errors),
                'employee_form_errors': json.dumps(employee_form.errors),
                'positions': positions
            })

    else:
        user_form = UserForm()
        employee_form = EmployeeForm()
    return render(request, 'add_employee.html', {
        'user_form': user_form,
        'employee_form': employee_form,
        'positions': positions
    })


def add_leave(request):
    if request.method == 'POST':
        leave_request_form = LeaveRequestForm(request.POST)

        if leave_request_form.is_valid():
            leave_request_form.save()
            return redirect('employees')
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


def leave_requests(request):
    leave_requests_list = LeaveRequest.objects.all().select_related('employee__user')
    context = {
        'leave_requests': leave_requests_list
    }
    return render(request, 'leave_requests.html', context)


@csrf_exempt
def add_position(request):
    if request.method == 'POST':
        position_name = request.POST.get('position_name')
        position = Position.objects.create(name=position_name)
        return JsonResponse({'position_id': position.id, 'position_name': position.name})


def positions(request):
    positions_list = Position.objects.all().annotate(employee_count=Count('employee'))
    context = {
        'positions': positions_list
    }
    return render(request, 'positions.html', context)


@csrf_exempt
def add_department(request):
    if request.method == 'POST':
        department_name = request.POST.get('department_name')
        department = Department.objects.create(name=department_name)
        return JsonResponse({'department_id': department.id, 'department_name': department.name})


def departments(request):
    departments_list = Department.objects.all()
    context = {
        'departments': departments_list
    }
    return render(request, 'departments.html', context)


def leave_types(request):
    leave_types_list = LeaveType.objects.all()
    paginator = Paginator(leave_types_list, 10)
    page_number = request.GET.get('page')
    page_leave_types = paginator.get_page(page_number)
    context = {
        'leave_types': page_leave_types
    }
    return render(request, 'leave_types.html', context)
