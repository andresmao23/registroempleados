from django.db import models
from applications.department.models import Department
from ckeditor.fields import RichTextField

# Create your models here.
class Skill(models.Model):
    skill = models.CharField('Habilidad', max_length=50, unique=True)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return self.skill

class Employee(models.Model):
    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro')
    )
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    job = models.CharField('Trabajo',max_length=1, choices=JOB_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    skills = models.ManyToManyField(Skill)
    curriculum = RichTextField(default='texto')

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return self.first_name + ' ' +self.last_name