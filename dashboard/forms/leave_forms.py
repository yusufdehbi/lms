from django import forms
from dashboard.models import LeaveRequest


class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['employee', 'leave_type', 'start_date', 'end_date', 'reason']
        widgets = {
            'employee': forms.Select(attrs={
                'class': 'js-select2 form-select',
                'data-placeholder': 'Select an employee'
            }),
            'leave_type': forms.Select(attrs={
                'class': 'js-select2 form-select',
                'data-placeholder': 'Select a leave type'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'js-flatpickr form-control',
                'placeholder': 'Select the start date'
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'js-flatpickr form-control',
                'placeholder': 'Select the end date'
            }),
            'reason': forms.Textarea(attrs={
                'class': 'form-control',
            })
        }
