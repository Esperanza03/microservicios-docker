from rest_framework import serializers
from .models import Evaluacion
import requests

class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = ['id', 'rut_estudiante', 'semestre', 'asignatura', 'evaluacion']
    
    def validate_rut_estudiante(self, value):
        # Verificar si el estudiante existe llamando al microservicio de estudiante
        estudiante_service_url = 'http://estudiante:8000/api/estudiantes/'
        
        try:
            response = requests.get(f"{estudiante_service_url}{value}/")
            if response.status_code == 404:
                raise serializers.ValidationError("El estudiante con este RUT no existe")
        except requests.RequestException:
            # Si hay un error de conexión, permitimos la creación pero advertimos
            pass
            
        return value