from rest_framework.serializers import ModelSerializer
from barberia.models import Turno


class TurnosSerializer(ModelSerializer):
    class Meta:
        model = Turno
        fields = ['fecha','especialidad','servicio','profesional','hora']