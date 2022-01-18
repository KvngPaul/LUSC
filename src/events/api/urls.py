from django.urls import path, include
from .views import (
    TransportListView,
    TransportMasterListView,
    TransportMasterCreateView,
    TransportMasterRUDView,

    #     Luggage View Import
    LuggageListView,
    LuggageMasterListView,
    LuggageMasterCreateView,
    LuggageMasterRUDView,


    #     TradeFairViews
    TradeFairListView,
    TradeFairMasterListView,
    TradeFairMasterCreateView,
    TradeFairMasterRUDView
)

app_name = 'event-api'

urlpatterns = [
    # Transport Event
    path("transport/", TransportListView.as_view(), name="transport-list"),

    # Luggage Event
    path("luggage/", LuggageListView.as_view(), name="luggage-list"),

    # Trade Fair Event
    path("tradefair/", TradeFairListView.as_view(), name="trade-fair-list"),


    # Master Series

    # Transport Event
    path("master/transport/", TransportMasterListView.as_view(),
         name="transport-list-master"),

    path("master/transport/create/", TransportMasterCreateView.as_view(),
         name="transport-create-master"),

    path("master/transport/<int:id>/",
         TransportMasterRUDView.as_view(), name="transport-rud-master"),

    # Luggage Event
    path("master/luggage/", LuggageMasterListView.as_view(),
         name="luggage-list-master"),

    path("master/luggage/create/", LuggageMasterCreateView.as_view(),
         name="luggage-create-master"),

    path("master/luggage/<int:id>/",
         LuggageMasterRUDView.as_view(), name="luggage-rud-master"),

    # Trade Fair Event
    path("master/tradefair/", TradeFairMasterListView.as_view(),
         name="trade-fair-list-master"),

    path("master/tradefair/create/", TradeFairMasterCreateView.as_view(),
         name="trade-fair-create-master"),

    path("master/tradefair/<int:id>/",
         TradeFairMasterRUDView.as_view(), name="trade-fair-rud-master"),
]
