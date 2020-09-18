from rest_framework import serializers

from common.models.manner_model import Manner


class MannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manner
        fields = '__all__'
        read_only_fields = ['id_member', 'cdate', 'udate']


class MannerCreateSerializer(MannerSerializer):
    class Meta:
        model = Manner
        fields = '__all__'
        read_only_fields = []
