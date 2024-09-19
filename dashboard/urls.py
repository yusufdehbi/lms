from django.urls import path
from debug_toolbar.toolbar import debug_toolbar_urls
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Employees
    path('employees/', views.employees, name='employees'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('employee/<int:employee_id>/', views.employee, name='employee'),
    path('add_position', views.add_position, name='add_position'),
    # Leaves
    path('add_leave/', views.add_leave, name='add_leave'),
    path('leave_requests/', views.leave_requests, name='leave_requests'),
    # Authentication
    path('login/', views.login, name="login")
] + debug_toolbar_urls()
