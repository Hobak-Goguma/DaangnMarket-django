from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from common.models.member_model import Member
from common.serializers.member_serializer import MemberTouchSerializer, MemberSerializer


@api_view(['GET', 'PUT'])
def member_info(request):
	"""
	코드 조각 조회, 업데이트, 삭제
	Modifiable List : nick_name, tel, email, birth, img, gender
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

	if request.method == 'GET':
		serializer = MemberSerializer(member)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = MemberTouchSerializer(member, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
