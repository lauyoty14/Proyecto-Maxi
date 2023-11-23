# api/urls.py
from core.urls import path
from .views import TurnoApiViewSet
from rest_framework.routers import DefaultRouter

# Define las acciones permitidas en el conjunto de vistas
my_api_viewset_actions = {'get': 'list', 'post': 'create'}

# Crea una vista para el conjunto de vistas con acciones permitidas
my_api_view = TurnoApiViewSet.as_view(my_api_viewset_actions)

# Configura el enrutador
router = DefaultRouter()
router.register(r'endpoint', TurnoApiViewSet, basename='my_api_endpoint')

# Agrega las rutas generadas por el enrutador
urlpatterns = router.urls

# Agrega una ruta manual para el método GET del conjunto de vistas
urlpatterns += [
    path('endpoint/', my_api_view, name='my_api_endpoint'),
    # Agrega otras rutas de la API según sea necesario
]
