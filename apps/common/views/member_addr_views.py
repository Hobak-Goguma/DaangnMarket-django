import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from common.models.location_model import Location
from common.models.member_addr_model import Memberaddr
from common.serializers.member_serializer import memberAddrSerializer


@api_view(['GET', 'DELETE'])
def member_addr(request, id_member):
    """
    멤버 주소 조회 수정, 삭제
    """
    # try:
    memberAddr = Memberaddr.objects.filter(id_member=id_member)
    if memberAddr.count() == 0:
        content = {
            "message": "사용자가 설정한 주소가 없습니다.",
            "result": {}
        }
        return Response(content, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = memberAddrSerializer(memberAddr, many=True)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        # 파라미터 get방식
        # Addr = request.GET['addr']

        # 제이슨 방식
        data = request.body.decode('utf-8')
        received_json_data = json.loads(data)
        Addr = received_json_data['addr']
        # 1개인 경우 삭제 불가
        if memberAddr.count() <= 1:
            content = {
                "message": "동네가 1개만 선택된 상태에서는 삭제를 할 수 없습니다.",
                "result": {"addr": Addr}
            }
            return Response(content, status=status.HTTP_202_ACCEPTED)
        # 삭제
        q = memberAddr.get(addr=Addr)
        q.delete()
        # 다른 주소는 Y로 변경
        Memberaddr.objects.filter(id_member=id_member).update(select="Y")
        content = {
            "message": "삭제 완료",
            "result": {"addr": Addr}
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def member_addr_create(request):
    """
    멤버 주소 생성
    """
    #  Data = json.loads(request.body)
    #     user_id = Data['user_id']
    #     user_pw = Data['user_pw']
    #     member = Member.objects.get(user_id = user_id, user_pw = user_pw)

    if request.method == 'POST':
        data = request.body.decode('utf-8')
        received_json_data = json.loads(data)
        id_member = received_json_data['id_member']
        addr = received_json_data['addr']
        Person = Memberaddr.objects.filter(id_member=id_member)
        # 주소 유효성 검사
        try:
            Location.objects.get(dong=addr)
        except Location.DoesNotExist:
            content = {
                "message": "없는 주소입니다",
                "result": {}
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        # Case 1. 주소가 0개인 회원
        if Person.count() == 0:
            serializer = memberAddrSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Case 2. 주소가 1개인 회원
        elif Person.count() == 1:
            # 중복체크
            try:
                overlap = Person.get(addr=addr)
                content = {
                    "message": "중복된 주소가 있습니다.",
                    "result": {"id_member = " + str(id_member): addr}
                }
            # 중복 없을 때
            except Memberaddr.DoesNotExist:
                # 기존에 있던 주소의 선택사항은 "선택안함"
                select = Person.get(id_member=id_member)
                select.select = "N"
                select.save()
                # 새로운 주소 등록
                serializer = memberAddrSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(content, status=status.HTTP_409_CONFLICT)
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        elif Person.count() >= 2:
            content = {
                "message": "허용된 주소의 갯수는 2개입니다.",
                "result": {}
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def member_addr_dis_update(request, id_member):
    """
    특정멤버 주소 선택 & 거리 견경
    """
    Data = json.loads(request.body)
    # 해당 멤버의 주소를 모두 N 으로 바꿈
    member = Memberaddr.objects.filter(id_member=id_member)
    member.update(select="N")
    addr = Data['addr']
    dis = Data['dis']
    # 거리값 유효성 검사
    if dis in [0, 2, 5, 10, 15]:
        # 받은 주소의 선택값 "Y", 거리 변경
        addrselect = member.get(addr=addr)
        addrselect.select = "Y"
        addrselect.distance = dis
        addrselect.save()
        serializer = memberAddrSerializer(member, many=True)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
    else:
        content = {
            "message": "없는 거리값입니다. 유효한 거리값 : 0, 2, 5, 10 ,15(단위 : km)",
            "result": {}
        }
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
