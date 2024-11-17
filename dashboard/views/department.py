from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from dashboard.models import User, Employee, Department, Position, LeaveRequest, LeaveType


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
    return render(request, 'pages/department/departments.html', context)
