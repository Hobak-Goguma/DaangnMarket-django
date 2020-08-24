from django.utils import timezone
from rest_framework import serializers

from common.models.member_model import Member


class LoginSerializer(serializers.ModelSerializer):
    last_date = serializers.DateTimeField(default=timezone.now)

    class Meta:
        model = Member
        fields = ('id_member', 'user_id', 'name', 'nick_name', 'tel', 'last_date', 'image')
