from rest_framework import serializers

from .models import Custumer


class CustumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custumer
        fields = ('id', 'first_name', 'last_name', 'date_of_birth')
        read_only_fields = ('id',)