from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Evaluacion(models.Model):
    rut_estudiante = models.CharField(max_length=12)
    semestre = models.CharField(max_length=10)
    asignatura = models.CharField(max_length=100)
    evaluacion = models.FloatField(
        validators=[
            MinValueValidator(1.0, 'La nota no puede ser menor a 1.0'),
            MaxValueValidator(7.0, 'La nota no puede ser mayor a 7.0')
        ]
    )
    
    def __str__(self):
        return f"{self.rut_estudiante} - {self.asignatura} - {self.evaluacion}"