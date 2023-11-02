from rest_framework.viewsets import ModelViewSet
from barberia.models import Turno
from barberia.api.seralizers import TurnosSeralizer

class TurnoApiViewSet(ModelViewSet):
    serializer_class = TurnosSeralizer
    queryset = Turno.objects.all()