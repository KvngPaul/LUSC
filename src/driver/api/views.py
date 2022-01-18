from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView, 
    RetrieveUpdateDestroyAPIView
    )

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from driver.models import Driver
from .serializers import DriverSerializer

class DriverCreateView(CreateAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class DriverListView(ListAPIView):
    queryset =  Driver.objects.all()
    serializer_class = DriverSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class DriverRUDView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
