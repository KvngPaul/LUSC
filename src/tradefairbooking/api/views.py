from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveDestroyAPIView
)

from luggages.models import Tent, TentRegister, ExtraMaster, TradeFairBooking
from events.models import TradeFairEvent
from .serializers import (
    TentSerializer,
    TentRegisterSerializer,
    TradeFairBookingSerializer
)

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Tent
class TentListView(ListAPIView):
    queryset = Tent.objects.all()
    serializer_class = TentSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


# Tent Master
class TentMasterCreateView(CreateAPIView):
    queryset = Tent.objects.all()
    serializer_class = TentSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class TentMasterRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Tent.objects.all()
    serializer_class = TentSerializer
    lookup_field = 'id'

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]



# Tent Register
class TentRegisterListView(ListAPIView):
    queryset = TentRegister.objects.active()
    serializer_class = TentRegisterSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


# Tent Register Master
class TentRegisterMasterCreateView(CreateAPIView):
    queryset = TentRegister.objects.active()
    serializer_class = TentRegisterSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]



class TentRegisterMasterRDView(RetrieveDestroyAPIView):
    queryset = TentRegister.objects.active()
    serializer_class = TentRegisterSerializer
    lookup_field = 'id'

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]


# Trade Fair Booking
class TradeFairBookingListView(ListAPIView):
    queryset = TradeFairBooking.objects.active()
    serializer_class = TradeFairBookingSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


# Trade Fair Booking Master
class TradeFairBookingMasterListView(ListAPIView):
    queryset = TradeFairBooking.objects.all()
    serializer_class = TradeFairBookingSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class TradeFairBookingMasterCreateView(CreateAPIView):
    queryset = TradeFairBooking.objects.all()
    serializer_class = TradeFairBookingSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        event = TradeFairEvent.objects.active()
        user = self.request.user
        if not user:
                raise ValidationError('You are not logged In')
        elif not event.exists():
            raise ValidationError(
                'You are currently not allowed to book your tradefair spot. Check back later.')
        else:
            serializer.save(user=user, event=event.latest('timestamp'))


class TradeFairBookingRegisterMasterRDView(RetrieveDestroyAPIView):
    queryset = TradeFairBooking.objects.all()
    serializer_class = TradeFairBookingSerializer
    lookup_field = 'id'

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]