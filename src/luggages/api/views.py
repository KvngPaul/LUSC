from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveDestroyAPIView
)

from luggages.models import Luggage, LuggageBooking
from events.models import LuggageEvent
from .serializers import (
    LuggageSerializer,
    LuggageBookingSerializer
)

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Luggage Active
class LuggageListView(ListAPIView):
    queryset = Luggage.objects.all()
    serializer_class = LuggageSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


# Luggage Master
class LuggageMasterCreateView(CreateAPIView):
    queryset = Luggage.objects.all()
    serializer_class = LuggageSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        booking = LuggageBooking.objects.active(user=self.request.user)
        if booking.exists():
            serializer.save(booking=booking.latest('timestamp'))
        else:
            event = LuggageEvent.objects.active()
            if not user:
                raise ValidationError('You are not logged In')
            elif not event.exists():
                raise ValidationError(
                    'You are currently unable to book your luggage. Check back later.')
            else:
                booking = LuggageBooking.objects.create(
                    user=user, event=event.latest('timestamp'))
                serializer.save(booking=booking)

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


class LuggageMasterRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Luggage.objects.all()
    serializer_class = LuggageSerializer
    lookup_field = 'id'

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


# Luggage Booking
class LuggageBookingListView(ListAPIView):
    queryset = LuggageBooking.objects.all()
    serializer_class = LuggageBookingSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


# Luggage Booking Master
class LuggageBookingMasterListView(ListAPIView):
    queryset = LuggageBooking.objects.all()
    serializer_class = LuggageBookingSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


class LuggageBookingMasterRDView(RetrieveDestroyAPIView):
    queryset = LuggageBooking.objects.all()
    serializer_class = LuggageBookingSerializer
    lookup_field = 'id'

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
