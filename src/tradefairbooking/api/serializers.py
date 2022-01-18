from rest_framework import serializers
from tradefairbooking.models import (
    Tent,
    TentRegister,
    ExtraMaster,
    TradeFairBooking
)
from tradefair.api.serializers import ExtraRegisterSerializer, GoodsRegisterSerializer
from accounts.api.serializers import UserSerializer


# Goods
class TentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tent
        fields = ['id',  'name', 'timestamp']
        read_only_fields = ['id', 'timestamp']


# Goods Register
class TentRegisterSerializer(serializers.ModelSerializer):
    tent_register = TentSerializer(many=False, read_only=True)

    class Meta:
        model = TentRegister
        fields = ['id', 'event', 'tent_register', 'price', 'note', 'slots', 'used_slots',
                  'available_slots', 'active', 'timestamp']
        read_only_fields = ['id', 'event', 'used_slots',
                            'available_slots', 'active', 'timestamp']


# Extra Master
class ExtraMasterSerializer(serializers.ModelSerializer):
    extra_set = ExtraRegisterSerializer(many=False, read_only=True)

    class Meta:
        model = ExtraMaster
        fields = ['id', 'extra_set', 'unit', 'total_price', 'timstamp']
        read_only_fields = ['id', 'extra_set',
                            'unit', 'total_price', 'timstamp']


# Trade Fair Booking
class TradeFairBookingSerializer(serializers.ModelSerializer):
    user_booking = UserSerializer(many=False, read_only=True)
    tent_booking = TentRegisterSerializer(many=False, read_only=True)
    goods_booking = GoodsRegisterSerializer(many=True, read_only=True)
    extra_booking = ExtraMasterSerializer(many=True, read_only=True)

    class Meta:
        model = TradeFairBooking
        fields = ['id', 'user_booking', 'event', 'tent_booking', 'goods_booking',
                  'extra_booking', 'total', 'active', 'approved', 'timestamp']
        read_only_fields = ['id', 'user_booking', 'event', 'tent_booking', 'goods_booking',
                            'extra_booking', 'total', 'active', 'timestamp']
