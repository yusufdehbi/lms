from django.urls import path
from django.contrib.auth import views as auth_views
from dashboard.forms.registration_forms import LoginForm
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
    # path('login/', views.login, name="login")
    path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm, template_name='registration/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    # Configuration
    path('positions/', views.positions, name='positions'),
    path('departments/', views.departments, name='departments'),
    path('add_department/', views.add_department, name='add_department'),
] + debug_toolbar_urls()
