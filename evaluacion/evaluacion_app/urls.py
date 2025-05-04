from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EvaluacionViewSet

router = DefaultRouter()
router.register(r'evaluaciones', EvaluacionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]