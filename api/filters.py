import django_filters
from .models import Mascota

class MascotaFilter(django_filters.FilterSet):

    min_edad = django_filters.NumberFilter(field_name='edad', lookup_expr='gte')
    max_edad = django_filters.NumberFilter(field_name='edad', lookup_expr='lte')

    sexo = django_filters.CharFilter(lookup_expr='icontains')
    raza = django_filters.CharFilter(lookup_expr='icontains')
    especie = django_filters.CharFilter(lookup_expr='icontains')

    class Meta: 
        model = Mascota
        fields = []
