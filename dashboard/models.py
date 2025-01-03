from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


# Create your models here.
class User(AbstractUser):
    ROLE_EMPLOYEE = 'employee'
    ROLE_HR_MANAGER = 'hr_manager'
    ROLE_DEPARTMENT_MANAGER = 'department_manager'
    ROLE_EXECUTIVE_MANAGER = 'executive_manager'
    ROLE_CHOICES = [
        (ROLE_EMPLOYEE, 'Employee'),
        (ROLE_HR_MANAGER, 'HR Manager'),
        (ROLE_DEPARTMENT_MANAGER, 'Department Manager'),
        (ROLE_EXECUTIVE_MANAGER, 'Executive Manager'),
    ]

    MALE = 'male'
    FEMALE = 'female'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]

    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    birthday = models.DateField(null=True, blank=True)

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee')
    groups = models.ManyToManyField(
        Group,
        related_name='user_set',
        blank=True,
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='user_ser',
        blank=True,
        verbose_name='user permissions',
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=100, unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.PROTECT)
    date_joined = models.DateField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.employee_id}"


class LeaveType(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    ANY = 'any'
    GENDER_RESTRICTION_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (ANY, 'any')
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    days_allocated = models.IntegerField()
    gender_restriction = models.CharField(max_length=10, choices=GENDER_RESTRICTION_CHOICES, default='any')

    def save(self, *args, **kwargs):
        if self.gender_restriction not in [choice[0] for choice in self.GENDER_RESTRICTION_CHOICES]:
            raise ValueError(f'Invalid gender restriction: {self.gender_restriction}')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class LeaveRequest(models.Model):
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    applied_on = models.DateTimeField(auto_now_add=True)
    approved_on = models.DateTimeField(blank=True, null=True)

    def numbers_of_days(self):
        return (self.end_date - self.start_date ).days + 1

    def __str__(self):
        return f"{self.employee} - {self.leave_type} ({self.start_date} to {self.end_date})"


class LeaveBalance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE)
    balance = models.IntegerField()

    def __str__(self):
        return f"{self.employee} - {self.leave_type}: {self.balance} days"
