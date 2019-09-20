import jwt

from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.utils.crypto import get_random_string

from ridemyway.settings import SECRET_KEY
from ridemyway.api.utilities.base_classes.models import BaseModel


class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, This is the same code used by
    Django to create a `User`. 
    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    def create_user(self, password=None, **data):
        """Create and return a `User` with an email, username and password."""

        user = self.model(**data)
        user.set_password(password)
        user.is_active = False
        user.save()

        return user

    def create_superuser(self, username, email, password):
        """
        Create and return a `User` with superuser powers.
        Superuser powers means that this use is an admin that can do anything
        they want.
      """
        if password is None:
            raise TypeError('Superusers must have a password.')

        id_number = self.create_id_number()
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            id_number=id_number
        )
        user.is_superuser = True
        user.is_active = False
        user.is_staff = True
        user.save()

        return user

    def create_id_number(self):
        """
        Creates an id_number for only super users. This is for database entry
        Returns:
        id_number (str): generated id
        """
        id_number = get_random_string(8).lower()
        if User.objects.filter(id_number=id_number).first():
            self.create_id_number()

        return id_number


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    """Model for User"""

    # When a user no longer wishes to use our platform,
    # we simply offer them a way to deactivate their accounts
    is_active = models.BooleanField(default=False)

    email = models.EmailField(unique=True, blank=False)
    username = models.CharField(unique=True, max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    id_number = models.CharField(max_length=50, unique=True, blank=False)
    image_url = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=128, blank=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', ]

    objects = UserManager()

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username

    @property
    def token(self):
        """
        Method for generating a jwt token and also
        appending a dynamic field token on a user model through the
        @property decorator
        """
        payload = {
            'id': str(self.id),
            'username': self.username,
            "exp": datetime.now() + timedelta(days=2)
        }
        return jwt.encode(payload, SECRET_KEY).decode('utf-8')
