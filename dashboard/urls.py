from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Employees
    path('employees/', views.employees, name='employees'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('employee/<int:employee_id>/', views.employee, name='employee'),
    # Leaves
    path('add_leave/', views.add_leave, name='add_leave'),
]
