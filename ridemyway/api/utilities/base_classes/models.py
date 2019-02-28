from uuid import uuid4

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(
        default=None,
        max_length=50,
        blank=True,
        null=True)

    class Meta:
        abstract = True

