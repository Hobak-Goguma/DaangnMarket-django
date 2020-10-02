import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

from common.models.member_model import Member
from common.models.manner_model import Manner
from common.serializers.manner_serializer import MannerSerializer, MannerCreateSerializer


class MannerViewSet(viewsets.ModelViewSet):
    queryset = Manner.objects.all()
    serializer_class = MannerSerializer
    lookup_field = 'id_member'

    # def list(self, request):
    #     try:
    #         queryset = self.queryset.get(id_member=request.headers['id_member'])
    #     except Manner.DoesNotExist:
    #         content = {
    #             "message": "해당 유저의 매너온도 입니다. (매너온도가 등록되지 않았습니다.)",
    #             "result": {"score": 36.5}
    #         }
    #         return Response(content, status=status.HTTP_202_ACCEPTED)
    #     serializer = MannerSerializer(queryset)
    #     content = {
    #         "message": "해당 유저의 매너온도 입니다.",
    #         "result": {"score": serializer.data['score']}
    #     }
    #     return Response(content, status=status.HTTP_202_ACCEPTED)

    def create(self, request):
        data = request.data.copy()
        data['id_member'] = int(request.headers['id-member'])
        serializer = MannerCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # detail
    def retrieve(self, request, id_member):
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
            return Response(content, status=status.HTTP_202_ACCEPTED)
        serializer = MannerSerializer(queryset)
        content = {
            "message": "해당 유저의 매너온도 입니다.",
            "result": {"score": serializer.data['score']}
        }

        return Response(content, status=status.HTTP_202_ACCEPTED)
