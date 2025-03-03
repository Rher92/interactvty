from django.contrib.auth import get_user_model
from django.db import models
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from devices.models import Device
from devices.serializer import DeviceSerializer


class CitiesViewSet(ListModelMixin, GenericViewSet):
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Device.objects.filter()
