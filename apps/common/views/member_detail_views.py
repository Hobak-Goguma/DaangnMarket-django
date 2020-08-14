from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from common.models.member_model import Member
from common.serializers.member_serializer import MemberSerializer, MemberReviseSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def member_detail(request, id_member):
    """
    개별 유저 조회, 업데이트, 삭제
    ---
    유저의 id_member를 통해 개별 조회, 업데이트, 삭제 합니다.
    """
    try:
        member = Member.objects.get(pk=id_member)
    except Member.DoesNotExist:
        content = {
            "message" : "없는 사용자 입니다.",
            "result" : {}
                }
        return Response(content, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MemberSerializer(member)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MemberReviseSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        member.delete()
        content = {
            "message" : "pk :" + id_member + " 삭제 완료",
            "result" : {}
                }
        return Response(content ,status=status.HTTP_204_NO_CONTENT)