from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from rest_framework.views import APIView

from common.models.location_model import Location

allow_sido = ["서울특별시"]


class SigunguList(APIView):
    """
    	특정 시, 도의 시군구 리스트 조회

    	---
    	특정 시, 도의 시군구 리스트를 조회합니다.
    	"""
    permission_classes = [AllowAny]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gu_list = list(Location.objects.values_list('gu', flat=True).distinct())

    @swagger_auto_schema(
        operation_id='sigungu_list',
        responses={
            200: 'Success',
            400: 'Not allow region'
        })
    def get(self, request, sido):
        gu_list = list(Location.objects.values_list('gu', flat=True).distinct())
        if sido not in allow_sido:
            content = {
                "message": "현재 " + str(allow_sido) + " 지역만 서비스 진행 중입니다 !",
                "result": {}
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        content = {
            "message": sido + "의 모든 시군구입니다.",
            "result": gu_list
        }
        return Response(content, status=status.HTTP_200_OK)


class EupmyundongList(APIView):
    """
    	특정 시군구의 읍면동 리스트 조회

    	---
    	특정 시군구의 읍면동 리스트를 조회합나디.
    """
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_id='sigungu_list',
        responses={
            200: 'Success',
            404: 'Not exist gu',
            400: 'Not allow region'
        })
    def get(self, request, sido, sigungu):
        gu = Location.objects.filter(gu=sigungu)
        dong_list = list(Location.objects.filter(gu=sigungu).values_list('dong', flat=True).distinct())

        if gu.count() == 0:
            content = {
                "message": "해당 구는 없습니다.",
                "result": {}
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        if sido not in allow_sido:
            content = {
                "message": "현재 " + str(allow_sido) + " 지역만 서비스 진행 중입니다 !",
                "result": {}
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        content = {
            "message": sigungu + "의 동 리스트입니다.",
            "result": {sigungu: dong_list}
        }
        return Response(content, status=status.HTTP_200_OK)


class SidoEupmyundongList(APIView):
    """
        특정 시도의 {시군구: 읍면동} 리스트 조회

        ---
        특정 시도의 {시군구: 읍면동} 리스트를 조회합나디.
    """
    permission_classes = [AllowAny]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gu_list = list(Location.objects.values_list('gu', flat=True).distinct())
        self.gu_dong_dict = dict.fromkeys(self.gu_list, [])
        for gu in self.gu_list:
            self.gu_dong_dict[gu] = list(Location.objects.filter(gu=gu).values_list('dong', flat=True).distinct())

    @swagger_auto_schema(
        operation_id='sigungu_list',
        responses={
            200: 'Success',
            400: 'Not allow region'
        })
    def get(self, request, sido):
        if sido not in allow_sido:
            content = {
                "message": "현재 " + str(allow_sido) + " 지역만 서비스 진행 중입니다 !",
                "result": {}
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        content = {
            "message": sido + " 의 읍면동 리스트 입니다.",
            "result": self.gu_dong_dict
        }
        return Response(content, status=status.HTTP_200_OK)

