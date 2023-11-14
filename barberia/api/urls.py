# api/urls.py
from barberia.api.urls import path
from .views import TurnoApiViewSet
from rest_framework.routers import DefaultRouter

my_api_viewset = TurnoApiViewSet.as_view({'get': 'list'})

router = DefaultRouter()
router.register(r'endpoint', TurnoApiViewSet, basename='my_api_endpoint')
urlpatterns = router.urls

urlpatterns = [
    #path('endpoint/',TurnoApiViewSet.as_view(), name='my_api_endpoint'),
    # Agrega otras rutas de la API según sea necesario
]

