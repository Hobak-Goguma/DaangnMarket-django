from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from common.models.member_model import Member


@api_view(['GET'])
def nick_name_overlap(request):
    """
    닉네임 값이 중복되는지 확인해줍니다.
    """
    try:
        Nick_name = request.GET['nick_name']
        member = Member.objects.get(nick_name = Nick_name)
    except Member.DoesNotExist:
        content = {
            "message" : "중복닉네임이 없습니다.",
            "result" : {}
                }
        return Response(content, status=status.HTTP_200_OK)

    content = {
            "message" : "중복닉네임이 있습니다.",
            "result" : {}
                }
    return Response(content, status=status.HTTP_409_CONFLICT)