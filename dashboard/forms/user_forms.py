from django import forms
from dashboard.models import User


class UserForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=User.GENDER_CHOICES,
        widget=forms.RadioSelect(attrs={
            'class': 'form-check-input'
        }),
        required=True,
        initial=User.MALE
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'birthday', 'gender']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'first name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'last name'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email'
            }),
            'birthday': forms.DateInput(attrs={
                'class': 'js-flatpickr form-control',
                'placeholder': 'Y-m-d'
            }),
        }
