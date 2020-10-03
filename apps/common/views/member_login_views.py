import json

from django.utils import timezone
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from common.models.member_model import Member
from common.serializers.login_serializer import LoginSerializer
from common.views.schema.member_login_schema import member_login_schema, member_login_example, member_login_post_schema


@swagger_auto_schema(method='post', request_body=openapi.Schema(
	type=openapi.TYPE_OBJECT,
	properties=member_login_schema,
	example=member_login_example,
	),
    responses={
    200: member_login_post_schema
    })
@api_view(['POST'])
@permission_classes([AllowAny])
def member_login(request):
    """
    멤버 로그인

    ---

    """
    if request.method == 'POST':
        try:
            Data = json.loads(request.body)
            user_id = Data['user_id']
            user_pw = Data['user_pw']
            member = Member.objects.get(user_id = user_id, user_pw = user_pw)

        except Member.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        member.last_date = timezone.now()
        member.save()

        serializer = LoginSerializer(member)
        return Response(serializer.data)
    # if request.method == 'POST':
    #     serializer = LoginSerializer(member, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response(serializer.data)


    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)