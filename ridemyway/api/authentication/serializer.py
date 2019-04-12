from rest_framework import serializers

from .models import User

from ..utilities.helpers.validators import validate_field
from ..utilities.helpers.regex_patterns import patterns
from ..utilities.helpers.error_messages import error_messages


class UserSerializer(serializers.ModelSerializer):
    """User model serializer"""
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'username',
                  'id_number', 'phone_number', 'image_url', 'token')

        read_only_fields = 'id',

    def validate_email(self, field):
        """Validates an email addess
        
        Args:
            field (str): value for email
        Raises:
            ValidationError: if provided email does not match the pattern
        Returns:
            field (str): email value if its valid
        """
        return validate_field(field,
                              patterns['email_pattern'],
                              error_messages['invalid_email'])

    def validate_username(self, field):
        """Validates username
        
        Args:
            field (str): value for username
        Raises:
            ValidationError: if provided username does not match the pattern
        Returns:
            field (str): username value if its valid
        """
        return validate_field(field,
                              patterns['username_pattern'],
                              error_messages['invalid_username'])

    def validate_id_number(self, field):
        """Validates an id_number
        
        Args:
            field (str): value for an id_number
        Raises:
            ValidationError: if provided id_number does not match the pattern
        Returns:
            field (str): id_number value if its valid
        """
        return validate_field(field,
                              patterns['id_number_pattern'],
                              error_messages['invalid_id_number'])

    def validate_phone_number(self, field):
        """Validates phone number
        
        Args:
            field (str): value for phone_number
        Raises:
            ValidationError: if provided phone_number does not match the pattern
        Returns:
            field (str): phone_number value if its valid
        """
        return validate_field(field,
                              patterns['phone_number_pattern'],
                              error_messages['invalid_phone_number'])

    def validate_password(self, field):
        """Validates password
        
        Args:
            field (str): value for password
        Raises:
            ValidationError: if provided password does not match the pattern
        Returns:
            field (str): password value if its valid
        """
        return validate_field(field,
                              patterns['password_pattern'],
                              error_messages['invalid_password'])
