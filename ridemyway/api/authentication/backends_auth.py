import jwt

from rest_framework import exceptions
from rest_framework.authentication import get_authorization_header, BaseAuthentication

from ridemyway.settings import SECRET_KEY
from ridemyway.api.authentication.models import User


class JWTAuthentication():

    def authenticate(self, request, **kwargs):
        token = kwargs['token'] if 'token' in kwargs else get_authorization_header(request)

        if not token:
            return None 

        try:
            decoded_token = jwt.decode(token, SECRET_KEY)

            user_id, username = decoded_token['id'], decoded_token['username']

            user = User.objects.filter(id=user_id, username=username)

            return user, token

        except jwt.InvalidTokenError or jwt.DecodeError:
            raise exceptions.AuthenticationFailed("Invalid token, Please provide a valid one")

        except jwt.ExpiredSignature:
            raise exceptions.AuthenticationFailed("Token expired Login again to get new one")
