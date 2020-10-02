from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from common.models.member_model import Member
from common.views.schema.member_overlap_schema import member_overlap_parameter


@permission_classes([AllowAny])
@swagger_auto_schema(method='get',
    manual_parameters= member_overlap_parameter,
    responses={
    200: '중복아이디가 없습니다.',
    409: '중복아이디가 있습니다.'
    })
@api_view(['GET'])
def member_overlap(request):
    """
    아이디 중복 확인

    ---
    아이디값이 중복되는지 확인해줍니다.
    """
    try:
        User_id = request.GET['user_id']
        member = Member.objects.get(user_id = User_id)
    except Member.DoesNotExist:
        content = {
            "message" : "중복아이디가 없습니다.",
            "result" : {}
                }
        return Response(content, status=status.HTTP_200_OK)

    content = {
            "message" : "중복아이디가 있습니다.",
            "result" : {}
                }
    return Response(content, status=status.HTTP_409_CONFLICT)

