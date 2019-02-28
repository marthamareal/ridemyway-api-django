from django.db import models
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