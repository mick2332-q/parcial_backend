from rest_framework import viewsets,filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Mascota
from .serializers import MascotaSerializer
from .filters import MascotaFilter

class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = MascotaFilter

    ordering_fields = ['edad','fecha_registro']
    ordering = ['id']
