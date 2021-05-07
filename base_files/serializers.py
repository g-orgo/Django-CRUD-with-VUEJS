from rest_framework import serializers
from .models import Garage_place

class GarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garage_place
        fields = '__all__'