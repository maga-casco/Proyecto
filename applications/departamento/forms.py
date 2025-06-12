from django import forms
from applications.departamento.models import Departamento
from .models import Departamento

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre', 'sigla', 'piso', 'oficina']