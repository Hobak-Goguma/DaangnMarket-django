from typing import List, Any

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from common.models.location_model import Location
from posts.serializers.location_serializer import LocationSerializer


class SigunguList(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gu_list = list(Location.objects.values_list('gu', flat=True).distinct())

    def get(self, request, sido):
        gu_list = list(Location.objects.values_list('gu', flat=True).distinct())
        allow_sido = ["서울특별시"]
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
    def __init__(self, sigungu, **kwargs):
        super().__init__(**kwargs)
        self.gu = Location.objects.filter(gu=sigungu)
        self.dong_list = list(Location.objects.filter(gu=sigungu).values_list('dong', flat=True).distinct())
        self.dong_list = list(Location.objects.filter(gu=sigungu).values_list('dong', flat=True).distinct())

    def get(self, request, sigungu):
        if self.gu.count() == 0:
            content = {
                "message": "해당 구는 없습니다.",
                "result": {}
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        allow_sido = ["서울특별시"]
        if self.sido not in allow_sido:
            content = {
                "message": "현재 " + str(allow_sido) + " 지역만 서비스 진행 중입니다 !",
                "result": {}
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        content = {
            "message": sigungu + "의 동 리스트입니다.",
            "result": {sigungu: self.dong_list}
        }
        return Response(content, status=status.HTTP_200_OK)


class SidoEupmyundongList(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gu_list = list(Location.objects.values_list('gu', flat=True).distinct())
        self.gu_dong_dict = dict.fromkeys(self.gu_list, [])
        for gu in self.gu_list:
            self.gu_dong_dict[gu] = list(Location.objects.filter(gu=gu).values_list('dong', flat=True).distinct())

    def get(self, request, sido):
        allow_sido = ["서울특별시"]
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



# @api_view(['GET'])
# def sigungu(request, sido):
#     """
#     시군구리스트 호출 API
#     """
#     gu_list = list(Location.objects.values_list('gu', flat=True).distinct())
#
#     allow_sido = ["서울특별시"]
#     if sido not in allow_sido:
#         content = {
#             "message": "현재 " + str(allow_sido) + " 지역만 서비스 진행 중입니다 !",
#             "result": {}
#         }
#         return Response(content, status=status.HTTP_400_BAD_REQUEST)
#
#     content = {
#         "message": sido + "의 모든 시군구입니다.",
#         "result": gu_list
#     }
#     return Response(content, status=status.HTTP_200_OK)


# @api_view(['GET'])
# def eupmyundong(request, sido, sigungu):
#     """
#     읍면동 리스트 호출 API
#     """
#     gu = Location.objects.filter(gu=sigungu)
#     if gu.count() == 0:
#         content = {
#             "message": "해당 구는 없습니다.",
#             "result": {}
#         }
#         return Response(content, status=status.HTTP_404_NOT_FOUND)
#
#     allow_sido = ["서울특별시"]
#     if sido not in allow_sido:
#         content = {
#             "message": "현재 " + str(allow_sido) + " 지역만 서비스 진행 중입니다 !",
#             "result": {}
#         }
#         return Response(content, status=status.HTTP_400_BAD_REQUEST)
#
#     dong_list = list(Location.objects.filter(gu=sigungu).values_list('dong', flat=True).distinct())
#
#     content = {
#         "message": sigungu + "의 동 리스트입니다.",
#         "result": {sigungu: dong_list}
#     }
#     return Response(content, status=status.HTTP_200_OK)


# @api_view(['GET'])
# def sido_eupmyundong_list(request, sido):
#     gu_list = list(Location.objects.values_list('gu', flat=True).distinct())
#
#     allow_sido = ["서울특별시"]
#     if sido not in allow_sido:
#         content = {
#             "message": "현재 " + str(allow_sido) + " 지역만 서비스 진행 중입니다 !",
#             "result": {}
#         }
#         return Response(content, status=status.HTTP_400_BAD_REQUEST)
#
#     gu_dong_dict = dict.fromkeys(gu_list, [])
#     for gu in gu_list:
#         gu_dong_dict[gu] = list(Location.objects.filter(gu=gu).values_list('dong', flat=True).distinct())
#
#     content = {
#         "message": sido + " 의 읍면동 리스트 입니다.",
#         "result": gu_dong_dict
#     }
#     return Response(content, status=status.HTTP_200_OK)