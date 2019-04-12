from django.db import models

import jwt
from datetime import datetime, timedelta

from ridemyway.settings import SECRET_KEY
from ridemyway.api.utilities.base_classes.models import BaseModel


class User(BaseModel):
    """Model for User"""

    email = models.EmailField(unique=True, blank=False)
    status = models.CharField(default='inactive', max_length=50)
    username = models.CharField(unique=True, max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    id_number = models.CharField(max_length=50, unique=True, blank=False)
    image_url = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=50, blank=False)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username

    @property
    def token(self):
        """Method for generating a jwt token and also 
        appending a dynamic field token on a user model through the @property decorator"""
        payload = {
            'id': str(self.id),
            'username': self.username,
            "exp": datetime.now() + timedelta(days=2)
        }
        return jwt.encode(payload, SECRET_KEY).decode('utf-8')
        