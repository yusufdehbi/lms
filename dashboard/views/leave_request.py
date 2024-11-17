from django.shortcuts import render, redirect
import json
from django.contrib.auth.decorators import login_required
from dashboard.models import User, LeaveRequest
from dashboard.forms.leave_forms import LeaveRequestForm


def add_leave(request):
    if request.method == 'POST':
        leave_request_form = LeaveRequestForm(request.POST)

        if leave_request_form.is_valid():
            leave_request_form.save()
            return redirect('leave_requests')
        else:
            return render(request, 'pages/leave_request/add_leave.html', {
                'leave_request_form': leave_request_form,
                'leave_request_form_errors': json.dumps(leave_request_form.errors)
            })
    else:
        leave_request_form = LeaveRequestForm()
    return render(request, 'pages/leave_request/add_leave.html', {
        'leave_request_form': leave_request_form
    })


@login_required
def leave_requests(request):
    leave_requests_list = LeaveRequest.objects.all().select_related('employee__user')
    context = {
        'leave_requests': leave_requests_list
    }
    if request.user.role == User.ROLE_HR_MANAGER:
        return render(request, 'pages/leave_request/leave_requests.html', context)
    elif request.user.role == User.ROLE_EXECUTIVE_MANAGER:
        return render(request, 'pages/leave_request/leave_requests_admin.html', context)
