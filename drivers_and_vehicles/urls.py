from rest_framework import routers
from .api import VehicleViewSet
from .api import DriverViewSet


router = routers.DefaultRouter()
router.register('drivers/driver', DriverViewSet, 'driverlist')
router.register('vehicles/vehicle', VehicleViewSet, 'vehiclelist')

urlpatterns = router.urls
