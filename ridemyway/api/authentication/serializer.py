from django.core import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

        read_only_fields = ('id')
