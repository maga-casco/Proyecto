from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Empleado, Departamento
from django.db.models import Q
from datetime import date
from django.urls import reverse_lazy
from .forms import EmpleadoForm

# INICIO
class IndexView(TemplateView):
    template_name = 'utilidades/home.html'

# FILTROS POR INPUT
class ListarEmpleados(ListView):
    model = Empleado
    template_name = "empleado/lista_empleados.html"
    context_object_name = 'lista_empleado'

    def get_queryset(self):
        queryset = Empleado.objects.select_related('trabajo', 'departamento').all()
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(
                Q(nombre__icontains=query) |
                Q(apellido__icontains=query) |
                Q(departamento__nombre__icontains=query) |
                Q(trabajo__trabajo__icontains=query)
            )
        return queryset

# LISTAR EMPLEADOS POR DEPARTAMENTO CON FILTRO
class ListarPorDepto(ListView):
    model = Empleado
    template_name = "empleado/listar_por_depto.html"
    context_object_name = 'object_list'

    def get_queryset(self):
        departamento = self.request.GET.get('departamento', '')
        queryset = Empleado.objects.select_related('departamento').all()
        if departamento:
            queryset = queryset.filter(departamento__nombre=departamento)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['departamentos'] = Departamento.objects.values_list('nombre', flat=True).distinct()
        return context
    
# MÁS DETALLES DEL EMPLEADO
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado/empleado_detail.html'

# CREAR EMPLEADO
class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado/empleado_form.html'
    success_url = reverse_lazy('lista_empleado')

# EDITAR/ACTUALIZAR EMPLEADO
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado/empleado_form.html'
    success_url = reverse_lazy('lista_empleado')

# ELIMINAR EMPLEADO
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleado/empleado_confirm_delete.html'
    success_url = reverse_lazy('lista_empleado')
