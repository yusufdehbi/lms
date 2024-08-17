from django import forms
from dashboard.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_id', 'department', 'position', 'date_joined']
