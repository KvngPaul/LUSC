from rest_framework import serializers
from tradefair.models import (
    Goods,
    GoodsRegister,
    Extra,
    ExtraRegister
)


# Goods
class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['id',  'name', 'goods_image', 'timestamp']
        read_only_fields = ['id', 'timestamp']


# Goods Register
class GoodsRegisterSerializer(serializers.ModelSerializer):
    goods_register = GoodsSerializer(many=False, read_only=True)

    class Meta:
        model = GoodsRegister
        fields = ['id', 'event', 'slots', 'used_slots',
                  'available_slots', 'active', 'goods_register', 'timestamp']
        read_only_fields = ['id', 'event', 'used_slots',
                            'available_slots', 'active', 'timestamp']


# Extra
class ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extra
        fields = ['id',  'name', 'extra_image', 'timestamp']
        read_only_fields = ['id', 'timestamp']


# Extra Register
class ExtraRegisterSerializer(serializers.ModelSerializer):
    extra_register = ExtraSerializer(many=False, read_only=True)

    class Meta:
        model = ExtraRegister
        fields = ['id', 'event', 'slots', 'used_slots',
                  'available_slots', 'active', 'extra_register', 'timestamp']
        read_only_fields = ['id', 'event', 'used_slots',
                            'available_slots', 'active', 'timestamp']
