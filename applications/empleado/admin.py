from django.contrib import admin
from atexit import register
from .models import Empleado, Habilidades, Rol
import csv
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import date
from django_ckeditor_5.widgets import CKEditor5Widget

# Register your models here.
admin.site.register(Habilidades)

# EXPORTAR CSV
def export_selected_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="empleados.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nombre ', 'Apellido ', 'Trabajo ', 'Departamento ', 'Fecha de Nacimiento '])

    for empleado in queryset:
        writer.writerow([
            empleado.nombre,
            empleado.apellido,
            empleado.email,
            empleado.fecha_nac,
            empleado.pais,
            empleado.trabajo,
            empleado.departamento,
         ])

    return response
export_selected_to_csv.short_description = "Exportar empleados seleccionados a CSV"

# EXPORTAR PDF
def export_selected_to_pdf(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="empleados.pdf"'

    p = canvas.Canvas(response)
    y = 800
    p.setFont("Helvetica", 12)
    p.drawString(100, y, "Lista de Empleados")

    y -= 30
    for empleado in queryset:
        p.drawString(100, y, f'{empleado.nombre} {empleado.apellido} {empleado.departamento}')
        y -= 20
        if y < 50:
            p.showPage()
            y = 800

    p.showPage()
    p.save()
    return response
export_selected_to_pdf.short_description = "Exportar empleados seleccionados a PDF"

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'apellido',
        'email',
        'fecha_nac',
        'calcularEdad',
        'pais',
        'trabajo',
        'departamento',
        'sueldo',
        'observaciones',
    )

    search_fields = ('apellido', 'nombre')

    list_filter = ('departamento', 'trabajo', 'pais', 'habilidades')

    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'observaciones': CKEditor5Widget(config_name='default'),
        }

    actions = [export_selected_to_csv, export_selected_to_pdf]
    
    def calcularEdad(self, obj):
        today = date.today()
        age = today.year - obj.fecha_nac.year - ((today.month, today.day) < (obj.fecha_nac.month, obj.fecha_nac.day))
        print(obj)
        return age
    
    calcularEdad.short_description = 'Edad'

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Rol)
