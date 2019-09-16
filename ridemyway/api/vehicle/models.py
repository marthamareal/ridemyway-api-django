from django.conf import settings
from django.db import models

from ridemyway.api.utilities.base_classes.models import BaseModel


class Vehicle(BaseModel):
    CAR='CR'
    BIKE='BK'
    CATEGORY = (
        (CAR, 'Car'),
        (BIKE, 'Bike'),
    )
    number_plate = models.CharField(max_length=20, unique=True)
    category = models.CharField(max_length=5, choices=CATEGORY, default=CAR)
    color = models.CharField(max_length=20, blank=True, null=True)
    make = models.CharField(max_length=20, null=True)
    model = models.CharField(max_length=20, null=True)
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="vehicles", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.number_plate
