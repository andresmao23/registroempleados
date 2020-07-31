from django.contrib import admin
from .models import Employee, Skill

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'job',
        'department',
        'full_name',
        'id',
    ]

    def full_name(self, obj):
        '''Definiendo mi propia función para el administrador de django'''
        return obj.first_name + ' ' + obj.last_name
    full_name.short_description = 'Nombre completo'

    search_fields = ('first_name', 'last_name')
    list_filter = ('department', 'job', 'skills',)
    filter_horizontal = ('skills',)

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Skill)
