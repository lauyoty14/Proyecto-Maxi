from rest_framework.viewsets import ModelViewSet
from barberia.models import Turno
from .serializers import TurnosSerializer
from rest_framework.response import Response
from rest_framework import status

class TurnoApiViewSet(ModelViewSet):
    serializer_class = TurnosSerializer
    queryset = Turno.objects.all()
    def list(self, request):
        # Lógica para manejar solicitudes GET
        try:
            # Supongamos que tienes un modelo llamado MyModel y deseas recuperar todos los objetos
            from barberia.models import Turno

            queryset = Turno.objects.all()
            # Puedes usar un serializador para convertir los objetos del modelo en datos JSON
            from .serializers import TurnosSerializer

            serializer = TurnosSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
