from django.shortcuts import render
from .models import Employee, Department, Position
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
    departments = Department.objects.all()
    positions = Position.objects.all()
    return render(request, 'add_employee.html', {
        'departments': departments,
        'positions': positions,
    })
