from django.conf import settings
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from jwt import decode
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from common.models.member_model import Member
from common.serializers.member_serializer import MemberTouchSerializer
from common.views.schema.member_touch_schema import member_touch_schema, member_touch_example


@swagger_auto_schema(method='put', request_body=openapi.Schema(
	type=openapi.TYPE_OBJECT,
	properties=member_touch_schema,
	example=member_touch_example,
	),
    responses={
    200: 'Member Information Modified Successfully.'
    })
@api_view(['put'])
def member_info(request):
	"""
	멤버 정보 수정

	---
	Modifiable List : nick_name, tel, email, birth, gender
	"""
	user_token = request.headers['Authorization'].split(' ')[1]
	token_decoded = decode(user_token, settings.SECRET_KEY, algorithms=['HS256'])

	try:
		member = Member.objects.get(auth=token_decoded['user_id'])
	except Member.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'PUT':
		serializer = MemberTouchSerializer(member, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
