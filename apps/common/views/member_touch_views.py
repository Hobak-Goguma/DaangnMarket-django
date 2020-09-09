from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from common.models.member_model import Member
from common.serializers.member_serializer import MemberTouchSerializer
from common.views.schema.member_touch_schema import member_touch_schema


@swagger_auto_schema(method='put', request_body=openapi.Schema(
	type=openapi.TYPE_OBJECT,
	properties=member_touch_schema,
	example={
		'nick_name' : 'ddusi',
		'tel' : '010-0000-0000',
		'birth' : '1994-03-30',
		'email' : 'ddusi@kakao.com',
		'gender' : 'MALE'
	}
))
@api_view(['put'])
def member_info(request):
	"""
	멤버 정보 수정

	---
	Modifiable List : nick_name, tel, email, birth, gender
	"""
	try:
		if 'id-member' in request.headers:
			member = Member.objects.get(id_member=request.headers['id-member'])
		else:
			content = {
				"message": "header정보가 없습니다.",
				"result": {}
			}
			return Response(content, status=status.HTTP_404_NOT_FOUND)

	except Member.DoesNotExist:
		content = {
			"message": "없는 사용자 입니다.",
			"result": {}
		}
		return Response(content, status=status.HTTP_404_NOT_FOUND)

	if request.method == 'PUT':
		serializer = MemberTouchSerializer(member, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
