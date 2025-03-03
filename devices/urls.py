from django.urls import path

# Views
from devices.views import CitiesViewSet

app_name = "devices"
urlpatterns = [
    path(route="", view=CitiesViewSet.as_view({'get': 'list'}), name="devices"),
]