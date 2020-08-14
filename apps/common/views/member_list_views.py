from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from common.models.member_model import Member
from common.serializers.member_serializer import MemberSerializer


# 'method' can be used to customize a single HTTP method of a view
@swagger_auto_schema(method='get', responses={200: 'OK'})
# 'methods' can be used to apply the same modification to multiple methods
@swagger_auto_schema(methods=['post'], request_body=MemberSerializer)
@api_view(['GET', 'POST'])
def member_list(request):
    """
    모든 유저 조회, 유저 등록
    ---
    모든 유저의 정보를 보여주거나 새 유저 정보를 등록합니다.
    """
    if request.method == 'GET':
        member = Member.objects.all()
        serializer = MemberSerializer(member, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @swagger_auto_schema(method='GET', responses={200:'OK'})
# 'methods' can be used to apply the same modification to multiple methods
# @swagger_auto_schema(methods=['post'], request_body=MemberSerializer)
