from django.contrib import admin
from django.urls import path
from .views import (ListAllEmployee, ListEmployeeByArea,
                    ListEmployeeByKword, ListEmployeSkill,
                    EmployeDetailView, EmployeeCreateView,
                    SuccessCreateView, EmployeeUpdateView,
                    EmployeeDeleteView, EmployeeSuccessDeleteView,
                    IndexView,
                    )

'''def employee(self):
    print('********************* SALUDOS DESDE LA APP EMPLEADO ************************')'''

app_name = 'employee_app'

urlpatterns = [
    #path('employee/', employee),
    path('', IndexView.as_view(), name='index'),
    path('list-all-employee/', ListAllEmployee.as_view(), name='list-all-employee'),
    path('list-employee-by-area/<short_name>', ListEmployeeByArea.as_view(), name='list-employee-by-area'),
    path('list-employee-by-kword/', ListEmployeeByKword.as_view(), name='list-employee-by-kword'),
    path('employee-skill/', ListEmployeSkill.as_view(), name='employee-skill'),
    path('employee-detail/<pk>', EmployeDetailView.as_view(), name='employee-detail'),
    path('employee-create/', EmployeeCreateView.as_view(), name='employee-create'),
    path('success-create/', SuccessCreateView.as_view(), name='success-create'),
    path('employee-update/<pk>', EmployeeUpdateView.as_view(), name='employee-update'),
    path('employee-delete/<pk>', EmployeeDeleteView.as_view(), name='employee-delete'),
    path('success-delete/', EmployeeSuccessDeleteView.as_view(), name='employee-success-delete'),
]
