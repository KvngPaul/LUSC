from rest_framework import serializers
from events.models import (
    TransportEvent,
    LuggageEvent,
    TradeFairEvent,
)


# Transport Event
class TransportEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportEvent
        fields = ['id', 'session', 'semester', 'start_date',
                  'end_date', 'payment_start_date', 'payment_end_date', 'transport_date', 'active', 'payment_active', 'timestamp']
        read_only_fields = ['active', 'payment_active', 'timestamp']


# Transport Event Master
class TransportEventMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportEvent
        fields = ['id', 'session', 'semester', 'start_date',
                  'end_date', 'payment_start_date', 'payment_end_date', 'transport_date', 'active', 'payment_active', 'timestamp']
        read_only_fields = ['active', 'payment_active', 'timestamp']


# Luggage Event
class LuggageEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = LuggageEvent
        fields = ['id', 'session', 'semester', 'start_date',
                  'end_date', 'deposit_start_date', 'deposit_end_date', 'deposit_note', 'active', 'deposit_active', 'timestamp']
        read_only_fields = ['active', 'deposit_active', 'timestamp']


# Luggage Event Master
class LuggageEventMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = LuggageEvent
        fields = ['id', 'session', 'semester', 'start_date',
                  'end_date', 'deposit_start_date', 'deposit_end_date', 'deposit_note', 'active', 'deposit_active', 'timestamp']
        read_only_fields = ['active', 'deposit_active', 'timestamp']


# Trade Fair Event
class TradeFairEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeFairEvent
        fields = ['id', 'session', 'theme', 'semester', 'start_date',
                  'end_date', 'fair_start_date', 'fair_end_date', 'fair_note', 'active', 'timestamp']
        read_only_fields = ['active', 'timestamp']


# Trade Fair Event Master
class TradeFairEventtMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeFairEvent
        fields = ['id', 'session', 'theme', 'semester', 'start_date',
                  'end_date', 'fair_start_date', 'fair_end_date', 'fair_note', 'active', 'timestamp']
        read_only_fields = ['active', 'timestamp']
