from django.db import models
from ..utilities.base_model import BaseModel


class User(BaseModel):

    email = models.EmailField(unique=True, blank=False)
    status = models.CharField(default='inactive', max_length=50)
    username = models.CharField(unique=True, max_length=50, blank=False)
    phone_number = models.CharField(max_length=15, blank=False)
    id_number = models.CharField(max_length=50, unique=True, blank=False)
    image_url = models.CharField(max_length=255, blank=True)
    
    
    class Meta:
        db_table = 'users'
