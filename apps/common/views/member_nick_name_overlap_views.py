from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from common.models.member_model import Member
from common.views.schema.member_overlap_schema import nick_name_overlap_parameter


@permission_classes([AllowAny])
@swagger_auto_schema(method='get',
    manual_parameters= nick_name_overlap_parameter,
    responses={
    200: '중복닉네임이 없습니다.',
    409: '중복닉네임이 있습니다.'
    })
@api_view(['GET'])
def nick_name_overlap(request):
    """
    닉네임 중복 확인

    ---
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