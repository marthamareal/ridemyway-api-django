from rest_framework import serializers

from ridemyway.api.vehicle.models import Vehicle
from ..utilities.helpers.validators import validate_field
from ..utilities.helpers.regex_patterns import patterns
from ..utilities.helpers.error_messages import error_messages


class VehicleSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source="user_id.email")

    class Meta:
        model = Vehicle

        extra_kwargs = {
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }

        fields = '__all__'
    
    def validate_number_plate(self, field):
        """Validates number_plate
        
        Args:
            field (str): value for number_plate
        Raises:
            ValidationError: if provided number_plate does not match the pattern
        Returns:
            field (str): number_plate value if its valid
        """
        return validate_field(field,
                              patterns['number_plate_pattern'],
                              error_messages['invalid_number_plate'])
