# Generated by Django 5.2 on 2025-05-07 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0006_empleado_email_empleado_observaciones_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Prueba',
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fecha_nac',
            field=models.DateField(default='2000-01-01', verbose_name='Fecha de Nacimiento'),
        ),
    ]
