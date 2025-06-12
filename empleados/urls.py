from django.contrib import admin
from django.urls import path, include
from applications.empleado.views import (IndexView, ListarPorDepto, ListarEmpleados, EmpleadoDetailView, EmpleadoCreateView, EmpleadoUpdateView, EmpleadoDeleteView)
from applications.departamento.views import DepartamentoListView, DepartamentoCreateView, DepartamentoDetailView, DepartamentoUpdateView, DepartamentoDeleteView

urlpatterns = [
    # ADMINISTRADOR Y HOME
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),

    # EMPLEADO
    path('lista_empleado/', ListarEmpleados.as_view(), name='lista_empleado'),
    path('empleado/crear/', EmpleadoCreateView.as_view(), name='empleado-crear'),
    path('empleado/<int:pk>/', EmpleadoDetailView.as_view(), name='empleado-detail'),
    path('empleado/editar/<int:pk>/', EmpleadoUpdateView.as_view(), name='empleado-editar'),
    path('empleado/eliminar/<int:pk>/', EmpleadoDeleteView.as_view(), name='empleado-eliminar'),

    # DEPARTAMENTO
    path('lista_departamento/', DepartamentoListView.as_view(), name='lista_departamento'),
    path('departamento/crear/', DepartamentoCreateView.as_view(), name='departamento-crear'),
    path('departamento/<int:pk>/', DepartamentoDetailView.as_view(), name='departamento-detail'),
    path('departamento/editar/<int:pk>/', DepartamentoUpdateView.as_view(), name='departamento-editar'),
    path('departamento/eliminar/<int:pk>/', DepartamentoDeleteView.as_view(), name='departamento-eliminar'),
    
    # FILTROS DE EMPLEADOS
    path('listar_por_depto/', ListarPorDepto.as_view()),
    path('listar_por_depto/<nombre>/', ListarPorDepto.as_view()),

    # CKEDITOR 5
    path('ckeditor5/', include('django_ckeditor_5.urls')),
]
