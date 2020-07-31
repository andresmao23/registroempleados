from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from applications.employee.models import Employee
from .models import Department
from .forms import DepartmentForm
from django.views.generic.edit import FormView

class DepartmentView(FormView):
    template_name = 'department/department_create.html'
    form_class = DepartmentForm
    success_url = reverse_lazy('employee_app:success-create')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        last_name = form.cleaned_data['last_name']
        department = form.cleaned_data['department']
        short_name = form.cleaned_data['short_name']
        depto = Department(name = department, short_name = short_name)
        depto.save()
        Employee.objects.create(
            first_name = name,
            last_name = last_name,
            job = '1',
            department = depto
        )
        return super().form_valid(form)

class ListAllDepartment(ListView):
    template_name = 'department/list_all_department.html'
    model = Department
    context_object_name = 'department_list'

