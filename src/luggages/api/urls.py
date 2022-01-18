from django.urls import path, include
from .views import (
    #     Luggage
    LuggageMasterCreateView,
    LuggageMasterRUDView,
    LuggageListView,

    # LuggageBooking
    LuggageBookingMasterListView,
    LuggageBookingMasterRDView,
    LuggageBookingListView
)

app_name = 'luggage-api'

urlpatterns = [
    # Luggage
    path("", LuggageListView.as_view(), name="luggage"),

    # Luggage Booking
    path("booking/", LuggageBookingListView.as_view(), name="luggage-booking"),


    # Master Series

    # Luggage

    path("master/create/", LuggageMasterCreateView.as_view(),
         name="luggage-master-create"),

    path("master/<int:id>/",
         LuggageMasterRUDView.as_view(), name="luggage-master-rud"),

    # Luggage Booking
    path("master/booking/", LuggageBookingMasterListView.as_view(),
         name="luggage-booking-master-list"),

    path("master/booking/<int:id>/",
         LuggageBookingMasterRDView.as_view(), name="luggage-booking-master-rud"),
]
