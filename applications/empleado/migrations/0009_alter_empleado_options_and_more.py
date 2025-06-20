# Generated by Django 5.2 on 2025-06-11 03:33

import django.db.models.deletion
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0008_alter_empleado_observaciones'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['apellido', 'nombre'], 'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados de la Empresa'},
        ),
        migrations.AlterUniqueTogether(
            name='habilidades',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='empleado',
            name='fecha_ingreso',
            field=models.DateField(default='2000-01-01', verbose_name='Fecha de Ingreso'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='sueldo',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=10),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='habilidades',
            field=models.ManyToManyField(blank=True, to='empleado.habilidades'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='observaciones',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='habilidades',
            name='habilidad',
            field=models.CharField(max_length=50, unique=True, verbose_name='Habilidad'),
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreRol', models.CharField(blank=True, max_length=40, verbose_name='trabajo')),
                ('habilidadesRol', models.ManyToManyField(blank=True, to='empleado.habilidades')),
            ],
            options={
                'verbose_name': 'Rol/Trabajo',
                'verbose_name_plural': 'Roles/Trabajos',
                'ordering': ['nombreRol'],
            },
        ),
        migrations.AlterField(
            model_name='empleado',
            name='trabajo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='empleado.rol', verbose_name='Rol/Trabajo'),
        ),
    ]
