from django.conf import settings
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
from jwt import decode
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from common.models.member_model import Member
from common.serializers.login_serializer import LoginSerializer
from common.views.schema.member_login_schema import member_login_post_schema


@swagger_auto_schema(method='post',
	 responses={
	     200: member_login_post_schema
	 })
@api_view(['POST'])
@permission_classes([AllowAny])
def member_login_views(request):
	"""
	멤버 토큰 정보로 유저정보 받아오기.

	---

	"""
	if request.method == 'POST':
		user_token = request.headers['Authorization'].split(' ')[1]
		token_decoded = decode(user_token, settings.SECRET_KEY, algorithms=['HS256'])

		try:
			member = Member.objects.get(auth=token_decoded['user_id'])
		except Member.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		member.last_date = timezone.now()
		member.save()

		return Response(LoginSerializer(member).data)
