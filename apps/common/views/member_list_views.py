from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from common.models.member_model import Member
from common.serializers.member_serializer import MemberSerializer


# @swagger_auto_schema(
# 	operation_id='member',
# 	request_body=MemberSerializer,
# 	responses={
# 		'200': MemberSerializer(),
# 	}
# )

class MemberListView(APIView):
	"""
	멤버 리스트 조회, 생성 API

	---
	POST
		- user_id
		- user_pw
		- name
		- tel
		- email
		- birth
		- gender
		- image
	"""
	def get(self, request, format=None):
		member = Member.objects.all()
		serializer = MemberSerializer(member, many=True, context={'request': request})
		return Response(serializer.data)

	@swagger_auto_schema(request_body=MemberSerializer)
	def post(self, request, format=None):
		serializer = MemberSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
