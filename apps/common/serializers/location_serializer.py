from rest_framework import serializers

from common.models.location_model import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('gu', 'dong')
