from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView, 
    RetrieveUpdateDestroyAPIView
    )
from destination.models import DestinationLink, Destination
from events.models import TransportEvent
from .serializers import (
    DestinationLinkSerializer, 
    DestinationLinkMasterSerializer, 
    DestinationSerializer
    )
from rest_framework import serializers



class DestinationLinkListView(ListAPIView):
    queryset = DestinationLink.objects.active()
    serializer_class = DestinationLinkSerializer

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class DestinationLinkCreateView(CreateAPIView):
    queryset = DestinationLink.objects.active()
    serializer_class = DestinationLinkSerializer

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    def perform_create(self, serializer):
        qs = TransportEvent.objects.filter(active=True)
        if not qs.exists():
            raise serializers.ValidationError("There is no active transport event. Transport Event must first be created.")
        elif qs.exists():
            serializer.save(event=TransportEvent.objects.active().latest('timestamp'))

class DestinationLinkRUDView(RetrieveUpdateDestroyAPIView):
    queryset = DestinationLink.objects.active()
    serializer_class = DestinationLinkSerializer
    lookup_field = 'id'

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


# Destination Link Master 

class DestinationLinkMasterListView(ListAPIView):
    queryset = DestinationLink.objects.event()
    serializer_class = DestinationLinkMasterSerializer

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class DestinationLinkMasterCreateView(CreateAPIView):
    queryset = DestinationLink.objects.event()
    serializer_class = DestinationLinkMasterSerializer

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    def perform_create(self, serializer):
        qs = DestinationLink.objects.event()
        if not qs.exists():
            raise serializers.ValidationError("There is no active transport event. Transport Event must first be created.")
        elif qs.exists():
            serializer.save(event=TransportEvent.objects.active().latest('timestamp'))

class DestinationLinkMasterRUDView(RetrieveUpdateDestroyAPIView):
    queryset = DestinationLink.objects.event()
    serializer_class = DestinationLinkMasterSerializer
    lookup_field = 'id'

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}



# Destination
class DestinationListView(ListAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


class DestinationCreateView(CreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


class DestinationRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    lookup_field = 'id'

    def get_serilaizer_context(self, *args, **kwargs):
        return {"request": self.request}