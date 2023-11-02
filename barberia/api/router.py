from rest_framework.routers import DefaultRouter
from barberia.api.views import TurnoApiViewSet

router_turnos = DefaultRouter()

router_turnos.register(prefix='turnos', basename='turnos', viewset=TurnoApiViewSet)
