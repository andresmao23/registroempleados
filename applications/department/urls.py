from django.contrib import admin
from django.urls import path
from .views import DepartmentView, ListAllDepartment

'''def department(self):
    print('********************* SALUDOS DESDE LA APP DEPARTMENT ************************')'''

app_name = 'department_app'

urlpatterns = [
    path('department-create/', DepartmentView.as_view(), name='department-create'),
    path('list-all-department/', ListAllDepartment.as_view(), name='list-all-department'),
]