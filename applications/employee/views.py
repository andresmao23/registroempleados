from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
        ListView, DetailView,
        CreateView, TemplateView,
        UpdateView, DeleteView
    )
from .models import Employee
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class ListAllEmployee(ListView):
    template_name = 'employee/list_all_employee.html'
    paginate_by = 4
    model = Employee
    '''context_object_name = 'employee_list'''

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        kword = self.request.GET.get('kword',)
        if kword:
            context['employee_list'] = Employee.objects.filter(
                Q(first_name=kword.capitalize()) | Q(last_name=kword.capitalize()))
        else:
            context['employee_list'] = Employee.objects.all()
        return context

class ListEmployeeByArea(ListView):
    '''Lista los empleados que pertenecen a un área específica'''
    #context_object_name = 'list_by_area'
    #queryset = Employee.objects.filter(department__short_name='Contabilidad')
    template_name = 'employee/list_employee_by_area.html'
    model = Employee

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        department = self.kwargs['short_name']
        # Add in the publisher
        context['list_by_area'] = Employee.objects.filter(department__short_name=department)
        return context

class ListEmployeeByKword(ListView):
    template_name = 'employee/list_employee_by_kword.html'
    model = Employee

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        kword = self.request.GET.get('kword',)
        if kword:
            context['list_by_kword'] = Employee.objects.filter(
                Q(first_name=kword.capitalize()) | Q(last_name=kword.capitalize()))
        else:
            context['list_by_kword'] = Employee.objects.filter(
                Q(first_name=kword) | Q(last_name=kword))
        return context

class ListEmployeSkill(ListView):
    template_name = 'employee/employee_skill.html'
    model = Employee

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        employee = Employee.objects.get(id=4)
        context['employee_skills'] = employee.skills.all()
        return context

class EmployeDetailView(DetailView):
    template_name = 'employee/employee_detail.html'
    context_object_name = 'employee'
    model = Employee

class SuccessCreateView(TemplateView):
    template_name = 'employee/success_create.html'

class EmployeeCreateView(CreateView):
    template_name = 'employee/employee_create.html'
    model = Employee
    fields = ('__all__')
    success_url = reverse_lazy('employee_app:success-create')

class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'employee/employee_update.html'
    fields = ('__all__')
    success_url = reverse_lazy('employee_app:success-create')

class EmployeeSuccessDeleteView(TemplateView):
    template_name = 'employee/success_delete.html'

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee/employee_delete.html'
    success_url = reverse_lazy('employee_app:employee-success-delete')