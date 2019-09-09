from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from ridemyway.api.vehicle.models import Vehicle
from ridemyway.api.vehicle.serializers import VehicleSerializer
from ridemyway.api.utilities.base_classes.views import BaseModelView


class VehicleView(BaseModelView):
    """Generic View for creating and listing all vehicles"""
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = VehicleSerializer
    model_name = "Vehicle"

    queryset = Vehicle.objects.all()

    def create(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied("You don't have permissions to carry out this action.")
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
