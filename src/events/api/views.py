from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    RetrieveUpdateDestroyAPIView
)

from events.models import TransportEvent, LuggageEvent, TradeFairEvent
from .serializers import (
    TransportEventSerializer,
    TransportEventMasterSerializer,
    LuggageEventSerializer,
    LuggageEventMasterSerializer,
    TradeFairEventSerializer,
    TradeFairEventtMasterSerializer
)

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Transport Event Active
class TransportListView(ListAPIView):
    queryset = TransportEvent.objects.active()
    serializer_class = TransportEventSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


# Transport Event Master
class TransportMasterListView(ListAPIView):
    queryset = TransportEvent.objects.all()
    serializer_class = TransportEventMasterSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


class TransportMasterCreateView(CreateAPIView):
    queryset = TransportEvent.objects.all()
    serializer_class = TransportEventMasterSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


class TransportMasterRUDView(RetrieveUpdateDestroyAPIView):
    queryset = TransportEvent.objects.all()
    serializer_class = TransportEventMasterSerializer
    lookup_field = 'id'

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


# Luggage Event
class LuggageListView(ListAPIView):
    queryset = LuggageEvent.objects.active()
    serializer_class = LuggageEventSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


# Luggage Event Master
class LuggageMasterListView(ListAPIView):
    queryset = LuggageEvent.objects.all()
    serializer_class = LuggageEventMasterSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


class LuggageMasterCreateView(CreateAPIView):
    queryset = LuggageEvent.objects.all()
    serializer_class = LuggageEventMasterSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


class LuggageMasterRUDView(RetrieveUpdateDestroyAPIView):
    queryset = LuggageEvent.objects.all()
    serializer_class = LuggageEventMasterSerializer
    lookup_field = 'id'

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


# Trade Fair Event
class TradeFairListView(ListAPIView):
    queryset = TradeFairEvent.objects.active()
    serializer_class = TradeFairEventSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


# Luggage Event Master
class TradeFairMasterListView(ListAPIView):
    queryset = TradeFairEvent.objects.all()
    serializer_class = TradeFairEventtMasterSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


class TradeFairMasterCreateView(CreateAPIView):
    queryset = TradeFairEvent.objects.all()
    serializer_class = TradeFairEventtMasterSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


class TradeFairMasterRUDView(RetrieveUpdateDestroyAPIView):
    queryset = TradeFairEvent.objects.all()
    serializer_class = TradeFairEventtMasterSerializer
    lookup_field = 'id'

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
