import json

from rest_framework import status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import viewsets

from common.models.manner_model import Manner
from common.serializers.manner_serializer import MannerSerializer


class MannerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Manner.objects.all()
    serializer_class = MannerSerializer
    lookup_field = 'id_member'

