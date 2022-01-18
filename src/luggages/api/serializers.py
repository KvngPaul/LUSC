from rest_framework import serializers
from luggages.models import (
    Luggage,
    LuggageBooking
)


# Luggage
class LuggageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Luggage
        fields = ['id',  'l_type', 'size',
                  'primary_color', 'secondary_color', 'deposited', 'date_deposited', 'collected', 'date_collected', 'timestamp']
        read_only_fields = ['date_deposited', 'date_collected', 'timestamp']

    def create(self, validated_data):
        lt = []
        for luggage in validated_data:
            l = Luggage.objects.create(**luggage)
            lt.append(l)
        return lt

    def update(self, instance, validated_date):
        lut = []
        for index, luggage in enumerate(validated_date):
            instance[index].l_type = luggage.get(
                'l_type', instance[index].l_type)
            instance[index].size = luggage.get(
                'size', instance[index].size)
            instance[index].primary_color = luggage.get(
                'primary_color', instance[index].primary_color)
            instance[index].secondary_color = luggage.get(
                'secondary_color', instance[index].secondary_color)
            instance[index].deposited = luggage.get(
                'deposited', instance[index].deposited)
            instance[index].collected = luggage.get(
                'collected', instance[index].collected)
            instance[index].save()
            lut.append(instance[index])
        return lut


# Luggage Booking
class LuggageBookingSerializer(serializers.ModelSerializer):
    luggage_booking = LuggageSerializer(many=True, read_only=True)

    class Meta:
        model = LuggageBooking
        fields = ['id', 'user', 'active', 'luggage_booking', 'timestamp']
        read_only_fields = ['active', 'event', 'timestamp']
