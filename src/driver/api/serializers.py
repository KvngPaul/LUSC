from rest_framework import serializers
from driver.models import Driver

class DriverSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Driver
        fields = ['uri', 'id', 'first_name', 'last_name', 'phone_number']
        read_only_fields = ['id']

    def get_uri(self, obj):
        request = self.context.get("request")
        return obj.get_api_uri(request=request)