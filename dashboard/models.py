from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    pass


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=100, unique=True)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    date_joined = models.DateField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.employee_id}"


class LeaveType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    days_allocated = models.IntegerField()

    def __str__(self):
        return self.name


class LeaveRequest(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('R', 'Rejected'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    applied_on = models.DateTimeField(auto_now_add=True)
    approved_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.employee} - {self.leave_type} ({self.start_date} to {self.end_date})"


class LeaveBalance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    balance = models.IntegerField()

    def __str__(self):
        return f"{self.employee} - {self.leave_type}: {self.balance} days"
