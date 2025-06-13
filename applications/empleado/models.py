from django.db import models
from applications.departamento.models import Departamento
from django_ckeditor_5.fields import CKEditor5Field
from datetime import date

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50, unique=True)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades de empleado'
        ordering = ['habilidad']

    def __str__(self):
        return self.habilidad
    

class Rol(models.Model):
    trabajo = models.CharField('trabajo', max_length=40, blank=True)
    habilidadesRol = models.ManyToManyField(Habilidades, blank=True)

    class Meta:
        verbose_name = 'Trabajo/Rol'
        verbose_name_plural = 'Trabajos/Roles'
        ordering = ['trabajo']

    def __str__(self):
        return self.trabajo

class Empleado(models.Model):
    nombre = models.CharField('Nombre', max_length=60)
    apellido = models.CharField('Apellido', max_length=60)
    fecha_nac = models.DateField('Fecha de Nacimiento', default='2000-01-01')
    pais = models.CharField('País', max_length=60, blank=True, null=True)
    trabajo = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True,blank=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2, default=1000)
    habilidades = models.ManyToManyField(Habilidades, blank=True)
    email = models.EmailField('Email', max_length=254, blank=True, null=True)
    observaciones = CKEditor5Field('Observaciones', config_name='default', blank=True)

    def edad(self):
        today = date.today()
        return today.year - self.fecha_nac.year - ((today.month, today.day) < (self.fecha_nac.month, self.fecha_nac.day))

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados de la Empresa'
        ordering = ['apellido', 'nombre']
        unique_together = ('nombre', 'departamento')

    def __str__(self):
        return f'{self.apellido} {self.nombre} - {self.trabajo}'
