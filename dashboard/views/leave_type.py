from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from dashboard.models import User, Employee, Department, Position, LeaveRequest, LeaveType
from django.core.paginator import Paginator


def leave_types(request):
    leave_types_list = LeaveType.objects.all()
    paginator = Paginator(leave_types_list, 10)
    page_number = request.GET.get('page')
    page_leave_types = paginator.get_page(page_number)
    context = {
        'leave_types': page_leave_types
    }
    return render(request, 'pages/leave_type/leave_types.html', context)


@csrf_exempt
def add_leave_type(request):
    if request.method == 'POST':
        name = request.POST.get('leave_type_name')
        description = request.POST.get('leave_type_description')
        days_allocated = request.POST.get('leave_type_days_allocated')
        gender = request.POST.get('leave_type_gender')

        leave_type = LeaveType.objects.create(name=name, description=description, days_allocated=days_allocated, gender_restriction=gender)
        return JsonResponse({'leave_type_id': leave_type.id, 'leave_type_name': leave_type.name})
