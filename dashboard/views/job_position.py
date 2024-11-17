from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from dashboard.models import Position


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
    return render(request, 'pages/job_position/positions.html', context)
