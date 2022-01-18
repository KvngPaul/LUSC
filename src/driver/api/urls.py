from django.urls import path, include

from .views import (
    DriverListView, 
    DriverCreateView, 
    DriverRUDView
    )

app_name = 'driver-api'

urlpatterns = [
    path('', DriverListView.as_view(), name="driver-list"),
    path('create/', DriverCreateView.as_view(), name="driver-create"),
    path('<int:id>/', DriverRUDView.as_view(), name="driver-rud"),
]