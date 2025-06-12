from django import forms
from applications.empleado.models import Empleado
from .models import Empleado, Departamento

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'email', 'fecha_nac', 'pais', 'trabajo', 'sueldo', 'departamento', 'observaciones']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['trabajo'].label = "Rol del Empleado"
        self.fields['departamento'].label = "Departamento"
        self.fields['departamento'].queryset = Departamento.objects.all()
