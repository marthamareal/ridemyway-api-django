from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.core.exceptions import ValidationError

from ridemyway.api.authentication.models import User
from ridemyway.api.authentication.serializer import UserSerializer, UserLoginSerializer
from ridemyway.api.utilities.helpers.renderers import ApiRenderer
from ridemyway.api.authentication.backends_auth import JWTAuthentication

from ..utilities.base_classes.views import BaseModelView, BaseSingleModelView


class UserView(BaseModelView):
    """ Generic view for creating and listing all users """
    permission_classes = (AllowAny,)
    queryset = User.objects.filter().all()
    serializer_class = UserSerializer
    model_name = 'User'

    def post(self, request, *args, **kwargs):
        """ Method for creating an object"""

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        response_data = {
            'message': 'Your account has been successfully created. An email has been sent to you with detailed instructions on how to activate it.',
            'status': status.HTTP_201_CREATED
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


class SingleUserView(BaseSingleModelView):
    """ Generic view for retrieving, updating and deleting a user """
    # permission_classes = (IsAuthenticated,)
    queryset = User.objects.filter().all()
    serializer_class = UserSerializer
    model_name = 'User'


class UserLoginView(generics.GenericAPIView):
    """ Generic view for loging in a user """
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer
    renderer_classes = ApiRenderer,

    def post(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class ActivateUserView(generics.GenericAPIView):
    """ Generic view for activating a user """
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer
    renderer_classes = ApiRenderer,

    def get(self, request, token):
        """ Method for activating a user"""

        authentication = JWTAuthentication()

        user =  authentication.authenticate(request, token=token)[0]

        if not user:
            raise ValidationError('Unable to activate your account, Please contact support')

        user.is_active = True
        user.save()

        response_data = {
            'status': 200,
            'message': 'Your account has been activated, You can now login with your email and password'
        }
        return Response(response_data, status=status.HTTP_200_OK)
