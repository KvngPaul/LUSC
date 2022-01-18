from rest_framework import serializers
from destination.models import DestinationLink, Destination
from locations.models import Town


class DestinationLinkSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    destination = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Destination.objects.all())
    
    class Meta:
        model = DestinationLink
        fields = ['uri', 'event', 'destination', 'total_seats', 'used_seats', 'available_seats']
        read_only_fields = ['available_seats', 'event', 'used_seats', 'total_seats']


    def get_uri(self, obj):
        request = self.context.get("request")
        return obj.get_api_uri(request=request, place='api:destination-api:destination-link-rud')

    def validate_event(self, value):
        if request.Method == 'POST':
            qs = TransportEvent.objects.active().latest('timestamp')
            if not qs.exists():
                raise serializers.ValidationError("There is no active transport event. Transport Event must first be created.")
            return value


# Destination Link Master
class DestinationLinkMasterSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    destination = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Destination.objects.all())
    
    class Meta:
        model = DestinationLink
        fields = ['uri', 'event', 'destination', 'total_seats', 'used_seats', 'available_seats', 'active']
        read_only_fields = ['available_seats', 'event', 'used_seats', 'total_seats', 'active']


    def get_uri(self, obj):
        request = self.context.get("request")
        return obj.get_api_uri(request=request, place='api:destination-api:destination-link-master-rud')

    def validate_event(self, value):
        if request.Method == 'POST':
            qs = TransportEvent.objects.active().latest('timestamp')
            if not qs.exists():
                raise serializers.ValidationError("There is no active transport event. Transport Event must first be created.")
            return value


# Destination 
class DestinationSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Destination
        fields =  ['uri', 'area', 'town']

    def get_uri(self, obj):
        request = self.context.get('request')
        return obj.get_api_uri(request=request, place='api:destination-api:destination-location-rud')