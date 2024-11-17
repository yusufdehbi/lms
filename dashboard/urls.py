from django.urls import path
from django.contrib.auth import views as auth_views
from dashboard.forms.registration_forms import LoginForm
from debug_toolbar.toolbar import debug_toolbar_urls
from .views.views import home
from .views.employee import employees, add_employee, employee
from .views.job_position import positions, add_position
from .views.department import departments, add_department
from .views.leave_request import leave_requests, add_leave
from .views.leave_type import leave_types, add_leave_type

urlpatterns = [
    path('', home, name='home'),

    # Employee
    path('employees/', employees, name='employees'),
    path('add_employee/', add_employee, name='add_employee'),
    path('employee/<int:employee_id>/', employee, name='employee'),

    # Job Position
    path('positions/', positions, name='positions'),
    path('add_position', add_position, name='add_position'),

    # Department
    path('departments/', departments, name='departments'),
    path('add_department/', add_department, name='add_department'),

    # Leave Request
    path('add_leave/', add_leave, name='add_leave'),
    path('leave_requests/', leave_requests, name='leave_requests'),

    # Leave Type
    path('add_leave_type/', add_leave_type, name='add_leave_type'),
    path('leave_types/', leave_types, name='leave_types'),

    # Authentication
    path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm, template_name='registration/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),

    # Configuration
] + debug_toolbar_urls()
