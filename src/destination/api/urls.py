from django.urls import path, include

from .views import (
    DestinationLinkListView, 
    DestinationLinkRUDView, 
    DestinationLinkCreateView,
    DestinationLinkMasterListView,
    DestinationLinkMasterCreateView,
    DestinationLinkMasterRUDView,
    DestinationListView,
    DestinationCreateView,
    DestinationRUDView
    )

app_name = 'destination-link-api'

urlpatterns = [
    # Destination Link
    path("", DestinationLinkListView.as_view(), name="destination-link-list"),
    path("create/", DestinationLinkCreateView.as_view(), name="destination-link-create"),
    path("<int:id>/", DestinationLinkRUDView.as_view(), name="destination-link-rud"),
    
    # Destination Link Master
    path("master/", DestinationLinkMasterListView.as_view(), name="destination-link-master-list"),
    path("master/create/", DestinationLinkMasterCreateView.as_view(), name="destination-link-master-create"),
    path("master/<int:id>/", DestinationLinkMasterRUDView.as_view(), name="destination-link-master-rud"),

    # Destination 
    path("location/", DestinationListView.as_view(), name="destination-location-list"),
    path("location/create/", DestinationCreateView.as_view(), name="destination-location-create"),
    path("location/<int:id>/", DestinationRUDView.as_view(), name="destination-location-rud"),
]