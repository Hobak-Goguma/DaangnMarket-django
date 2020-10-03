import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from common.views.schema.received_manner_detail_schema import received_manner_example, received_manner_schema, received_manner_parameter

from common.models.member_model import Member
from common.models.manner_model import Manner
from common.serializers.manner_serializer import MannerSerializer, MannerCreateSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated


class MannerViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Manner.objects.all()
    serializer_class = MannerSerializer
    lookup_field = 'id_member'
    http_method_names = ['get', 'post', 'put']

    def get_permissions(self):
        if self.action == 'retrieve':
            return [permission() for permission in [AllowAny]]
        else:
            return [permission() for permission in [IsAuthenticated]]

    @swagger_auto_schema(
        manual_parameters=received_manner_parameter,
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties=received_manner_schema,
            example=received_manner_example,
            required=['score']
        ),
        responses={
            201: 'Successfully created.',
            400: 'Bad Request'
        }
    )
    def create(self, request):
        """
        특정 멤버의 매너온도 생성 API

        ---
        """
        if self.queryset.filter(id_member=request.headers['id-member']).count() > 0:
            content = {
                "message": "이미 매너온도가 등록됨",
                "result": {}
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        data = request.data.copy()
        data['id_member'] = int(request.headers['id-member'])
        serializer = MannerCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={
            200: 'Success',
            400: '등록되지 않은 유저'
        }
    )
    def retrieve(self, request, id_member):
        """
        특정 멤버의 매너온도 조회 API

        ---
        """
        try:
            Member.objects.get(id_member=id_member)
        except Member.DoesNotExist:
            content = {
                "message": "등록되지 않은 유저입니다.",
                "result": {}
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        try:
            queryset = self.queryset.get(id_member=id_member)
        except Manner.DoesNotExist:
            content = {
                "message": "해당 유저의 매너온도 입니다. (매너온도가 등록되지 않았습니다.)",
                "result": {"score": 36.5}
            }
            return Response(content)
        serializer = MannerSerializer(queryset)
        content = {
            "message": "해당 유저의 매너온도 입니다.",
            "result": {"score": serializer.data['score']}
        }

        return Response(content)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties=received_manner_schema,
            example=received_manner_example,
            required=['score']
        ),
        responses={
            200: 'Successfully updated.'
        }
    )
    def update(self, request, id_member):
        """
        특정 멤버의 매너온도 수정 API

        ---
        """
        result = super(MannerViewSet, self).update(request, id_member)
        return Response(result.data)

