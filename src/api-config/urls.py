from django.urls import path, include


app_name = 'api'
urlpatterns = [
    path("login/", include('accounts.api.urls', namespace='user-api')),
    # path("driver/", include('driver.api.urls', namespace='driver-api')),
    # path("destination/", include('destination.api.urls', namespace='destination-api')),
    path("event/", include('events.api.urls', namespace='event-api')),
    path("luggage/", include('luggages.api.urls', namespace='luggage-api')),
    path("tradefair/", include('tradefair.api.urls', namespace='tradefair-api'))
]
