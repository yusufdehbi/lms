from django.contrib import admin
from dashboard.models import User, Employee, LeaveType, LeaveRequest, LeaveBalance
# Register your models here.
admin.site.register(User)
admin.site.register(Employee)
admin.site.register(LeaveType)
admin.site.register(LeaveRequest)
admin.site.register(LeaveBalance)
