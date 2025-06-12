from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField('Nombre', max_length=50, blank=True)
    sigla = models.CharField('Sigla', max_length=30)
    activo = models.BooleanField('¿Está activo?', default=False)
    piso = models.CharField('Piso', max_length=5, blank=True)
    oficina = models.CharField('Oficina N°', max_length=10, blank=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Departamentos'
        ordering = ['-nombre'] # Ordena alfabeticamente por nombre y si le agregas un - es descendente
        unique_together = ('nombre','sigla') # No permite que se registre un atributo 2 veces
    
    def __str__(self):
        return f"{self.nombre}"
