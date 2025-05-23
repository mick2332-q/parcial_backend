from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MascotaViewSet

# Crear un enrutador y registrar el viewset de Animal
router = DefaultRouter()
router.register(r'mascotas', MascotaViewSet)

# Incluir las URLs del enrutador en las rutas del proyecto
urlpatterns = [
    path('', include(router.urls)),
]
