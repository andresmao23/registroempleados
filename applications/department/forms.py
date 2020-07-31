from django import forms

class DepartmentForm(forms.Form):
    '''Datos del empleado'''
    name = forms.CharField(label='Nombres', widget=forms.TextInput(
                            attrs={'placeholder': 'Nombres del empleado'}),
                            error_messages={'required': 'Digite los nombres del empleado'}
                           )
    last_name = forms.CharField(label='Apellidos', widget=forms.TextInput(
                                attrs={'placeholder': 'Apellidos del empleado'}),
                                error_messages={'required': 'Digite los apellidos del empleado'}
                                )
    '''Datos del departamendo'''
    department = forms.CharField(label='Nombre del departamento', widget=forms.TextInput(
                                attrs={'placeholder': 'Nombre del departamento'}),
                                error_messages={'required': 'Digite el nombre del departamento'}
                                 )
    short_name = forms.CharField(label='Nombre corto', widget=forms.TextInput(
                                attrs={'placeholder': 'Nombre corto departamento'}),
                                error_messages={'required': 'Digite un nombre corto para el departamento'}
                                 )
