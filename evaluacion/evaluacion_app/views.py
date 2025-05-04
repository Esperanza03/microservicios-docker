from rest_framework import viewsets
from .models import Evaluacion
from .serializers import EvaluacionSerializer

class EvaluacionViewSet(viewsets.ModelViewSet):
    queryset = Evaluacion.objects.all()
    serializer_class = EvaluacionSerializer