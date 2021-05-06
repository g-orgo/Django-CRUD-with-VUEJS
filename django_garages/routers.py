from rest_framework import routers
from base_files.viewsets import GarageViewSet

router = routers.DefaultRouter()

router.register(r'garages', GarageViewSet)