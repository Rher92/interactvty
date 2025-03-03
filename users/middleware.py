import re

from django.contrib.auth import get_user_model
from django.utils.deprecation import MiddlewareMixin

from devices.models import Device

User = get_user_model()


class DeviceLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.user.is_authenticated:
            return

        ip = request.META.get("HTTP_X_FORWARDED_FOR")
        if ip:
            ip = ip.split(",")[0].strip()
        else:
            ip = request.META.get("REMOTE_ADDR")

        user_agent = request.META.get("HTTP_USER_AGENT", "Unknown")

        device, created = Device.objects.get_or_create(
            user=request.user, name=user_agent, defaults={"is_active": True, "ip": ip}
        )

        if not created:
            device.is_active = True
            device.save()
