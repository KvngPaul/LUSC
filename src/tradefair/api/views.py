from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from tradefair.models import Goods, GoodsRegister, Extra, ExtraRegister
from events.models import LuggageEvent
from .serializers import (
    GoodsSerializer,
    GoodsRegisterSerializer,
    ExtraSerializer,
    ExtraRegisterSerializer
)

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Goods
class GoodsListView(ListAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


# Goods Master
class GoodsMasterCreateView(CreateAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


class GoodsMasterRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    lookup_field = 'id'

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


# Goods Register
class GoodsRegisterListView(ListAPIView):
    queryset = GoodsRegister.objects.active()
    serializer_class = GoodsRegisterSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


# Goods Register Master
class GoodsRegisterMasterListView(ListAPIView):
    queryset = GoodsRegister.objects.all()
    serializer_class = GoodsRegisterSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


class GoodsRegisterMasterCreateView(CreateAPIView):
    queryset = GoodsRegister.objects.all()
    serializer_class = GoodsRegisterSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


class GoodsRegisterMasterRDView(RetrieveUpdateDestroyAPIView):
    queryset = GoodsRegister.objects.all()
    serializer_class = GoodsRegisterSerializer
    lookup_field = 'id'

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


# Extra
class ExtraListView(ListAPIView):
    queryset = Extra.objects.all()
    serializer_class = ExtraSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


# Extra Master
class ExtraMasterCreateView(CreateAPIView):
    queryset = Extra.objects.all()
    serializer_class = ExtraSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


class ExtraMasterRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Extra.objects.all()
    serializer_class = ExtraSerializer
    lookup_field = 'id'

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


# Extra Register
class ExtraRegisterListView(ListAPIView):
    queryset = ExtraRegister.objects.active()
    serializer_class = ExtraRegisterSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


# Extra Register Master
class ExtraRegisterMasterListView(ListAPIView):
    queryset = ExtraRegister.objects.all()
    serializer_class = ExtraRegisterSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


class ExtraRegisterMasterCreateView(CreateAPIView):
    queryset = ExtraRegister.objects.all()
    serializer_class = ExtraRegisterSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


class ExtraRegisterMasterRDView(RetrieveUpdateDestroyAPIView):
    queryset = ExtraRegister.objects.all()
    serializer_class = ExtraRegisterSerializer
    lookup_field = 'id'

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}
