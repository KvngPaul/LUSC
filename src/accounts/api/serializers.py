from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['reg_no', 'is_active', 'is_staff', 'is_admin']
        read_only_fields = ['reg_no', 'is_active', 'is_staff', 'is_admin']
