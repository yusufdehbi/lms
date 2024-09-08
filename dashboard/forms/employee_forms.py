from django import forms
from dashboard.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_id', 'department', 'position', 'date_joined']
        widgets = {
            'employee_id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'employee id'
            }),
            'department': forms.Select(attrs={
                'class': 'js-select2 form-select',
                'data-placeholder': 'Choose department'
            }),
            'position': forms.Select(attrs={
                'class': 'js-select2 form-select',
                'data-placeholder': 'Choose position',
                'id': 'positions-select'
            }),
            'date_joined': forms.DateInput(attrs={
                'class': 'js-flatpickr form-control',
                'placeholder': 'Y-m-d'
            }),
        }


