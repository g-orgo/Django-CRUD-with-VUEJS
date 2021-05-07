from rest_framework import viewsets
from .models import Garage_place
from .serializers import GarageSerializer

class GarageViewSet(viewsets.ModelViewSet):
    queryset = Garage_place.objects.all()
    serializer_class = GarageSerializer