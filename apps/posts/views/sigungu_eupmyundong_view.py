from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from posts.serializers.location_serializer import LocationSerializer
from common.models.location_model import Location


@api_view(['GET'])
def sigungu(request, sido):
    """
    시군구리스트 호출 API
    """
    gu_list = list(Location.objects.values_list('gu', flat=True).distinct())

    allow_sido = ["서울특별시"]
    if not (sido in allow_sido):
        content = {
            "message": "현재 " + str(allow_sido) + " 지역만 서비스 진행 중입니다 !",
            "result": {}
        }
        return Response(content)

    content = {
        "message": sido + "의 모든 시군구입니다.",
        "result": gu_list
    }
    return Response(content)


@api_view(['GET'])
def eupmyundong(request, sido, sigungu):
    """
    읍면동 리스트 호출 API
    """
    gu = Location.objects.filter(gu=sigungu)
    if gu.count() == 0:
        content = {
            "message": "해당 구는 없습니다.",
            "result": {}
        }
        return Response(content)

    allow_sido = ["서울특별시"]
    if not (sido in allow_sido):
        content = {
            "message": "현재 " + str(allow_sido) + " 지역만 서비스 진행 중입니다 !",
            "result": {}
        }
        return Response(content)

    dong_list = list(Location.objects.values_list('dong', flat=True).filter(gu=sigungu).distinct())

    content = {
        "message": sigungu + "의 동 리스트입니다.",
        "result": {sigungu: dong_list}
    }
    return Response(content)


@api_view(['GET'])
def sido_eupmyundong_list(request, sido):
    gu_list = list(Location.objects.values_list('gu', flat=True).distinct())

    gu_dong_dict = dict.fromkeys(gu_list, [])
    for gu in gu_list:
        gu_dong_dict[gu] = list(Location.objects.values_list('dong', flat=True).filter(gu=gu).distinct())

    content = {
        "message": sido + " 의 읍면동 리스트 입니다.",
        "result": gu_dong_dict
    }
    return Response(content)