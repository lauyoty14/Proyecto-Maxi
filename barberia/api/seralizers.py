from rest_framework.serializers import ModelSerializer
from barberia.models import Turno


class TurnosSeralizer(ModelSerializer):
    class Meta:
        model = Turno
        fields = ['fecha','especialidad','servicio','profesional','hora']