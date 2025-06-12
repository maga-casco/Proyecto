from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Departamento
from django.urls import reverse_lazy
from .forms import DepartamentoForm

# Create your views here.
class DepartamentoListView(ListView):
    model = Departamento
    template_name = 'departamento/lista_departamentos.html'
    context_object_name = 'lista_departamento'

# MÁS DETALLES DEL DEPARTAMENTO
class DepartamentoDetailView(DetailView):
    model = Departamento
    template_name = 'departamento/departamento_detail.html'

# CREAR DEPARTAMENTO
class DepartamentoCreateView(CreateView):
    model = Departamento
    template_name = 'departamento/departamento_form.html'
    form_class = DepartamentoForm
    success_url = reverse_lazy('lista_departamento')

# EDITAR/ACTUALIZAR DEPARTAMENTO
class DepartamentoUpdateView(UpdateView):
    model = Departamento
    template_name = 'departamento/departamento_form.html'
    form_class = DepartamentoForm
    success_url = reverse_lazy('lista_departamento')

# ELIMINAR DEPARTAMENTO
class DepartamentoDeleteView(DeleteView):
    model = Departamento
    template_name = 'departamento/departamento_confirm_delete.html'
    success_url = reverse_lazy('lista_departamento')