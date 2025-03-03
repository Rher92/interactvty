import logging
from utils.models import BaseModel

from django.db import models
from django.contrib.auth import get_user_model



logger = logging.getLogger(__name__)

User = get_user_model()

class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    ip = models.GenericIPAddressField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name