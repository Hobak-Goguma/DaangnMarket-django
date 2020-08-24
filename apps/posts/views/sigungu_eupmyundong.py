from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from posts.serializers.location_serializer import LocationSerializer
from common.models.location_model import Location

@api_view(['GET'])
def sigungu(request,sido):
    """
    시군구리스트 호출 API
    """
    # gu = request.GET['gu']

    gu = Location.objects.all()
    serializer = LocationSerializer(gu, many=True)

    # type : list [ 시군구 리스트 ]
    gu_list = list(set([i['gu'] for i in serializer.data]))

    if sido == '' :
        content = {
            "message" : "시도를 입력해주세요",
            "result" : {}
        }
        return Response(content)

    if sido != "서울특별시":
        content = {
            "message" : "현재 서울특별시만 서비스 진행 중입니다 !",
            "result" : {}
        }
        return Response(content)


    content = {
            "message" : sido +"의 모든 시군구입니다.",
            "result" : gu_list
    }
    return Response(content)


@api_view(['GET'])
def eupmyundong(request, sido, sigungu):
    """
    읍면동 리스트 호출 API
    """

    if sido != "서울특별시" :
        content = {
            "message" : "현재 서울특별시만 서비스 진행 중입니다 !",
            "result" : {}
        }
        return Response(content)


    gu = Location.objects.all()
    serializer = LocationSerializer(gu, many=True)
    # type : list [ 구 리스트 ]
    gu_list = list(set([i['gu'] for i in serializer.data]))

    # type : dict   { 시군구 : [읍면동 리스트] }
    gu_dong_dict = dict.fromkeys(gu_list, [])
    for i in gu_list:
        temp = []
        for j in serializer.data:
            if j['gu'] == i :
                temp.append(j['dong'])
                gu_dong_dict[i] = temp
    
    if sigungu is None:
        content = {
            "message" : "구를 입력하지 않음",
            "result" : gu_dong_dict
        }
        return Response(content)
    
    if gu_dong_dict.get(sigungu) is None :
        content = {
            "message" : "해당 구는 없습니다.",
            "result" : { }
        }
        return Response(content)

    content = {
            "message" : sigungu + "의 동 리스트입니다.",
            "result" :  { sigungu : gu_dong_dict[sigungu] }
        }
    return Response(content)


@api_view(['GET'])
def eupmyundong_check(request, sido):

    gu = Location.objects.all()
    serializer = LocationSerializer(gu, many=True)
    gu_list = list(set([i['gu'] for i in serializer.data]))

    content = {
    "message" : "시도 / 시군구 를 입력해주세요",
    "result" : { "sigungu" : gu_list }
    }
    return Response(content)

@api_view(['GET'])
def eupmyundong_check2(request):
    content = {
    "message" : "시도 / 시군구 를 입력해주세요",
    "result" : {}
    }
    return Response(content)