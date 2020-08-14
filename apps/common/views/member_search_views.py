from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from common.models.member_model import Member
from common.serializers.member_serializer import MemberSerializer


@api_view(['GET'])
def member_search(request):
    """
    특정유저를 아이디로 검색합니다.
    """
    try:
        User_id = request.GET['user_id']
        member = Member.objects.get(user_id = User_id)
    except Member.DoesNotExist:
        content = {
            "message" : "유저를 찾을 수 없습니다.",
            "result" : {}
                }
        return Response(content, status=status.HTTP_404_NOT_FOUND)

    serializer = MemberSerializer(member)
    return Response(serializer.data)