from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from common.models.member_model import Member
from common.serializers.member_serializer import MemberSerializer, MemberReviseSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


class MemberDetail(APIView):
	"""
	개별 유저 조회, 업데이트, 삭제
	---
	유저의 id_member를 통해 개별 조회, 업데이트, 삭제 합니다.
	"""

	def get(self, request, id_member, *args, **kwargs):
		try:
			self.member = Member.objects.get(id_member=id_member)
		except Member.DoesNotExist:
			content = {
				"message": "없는 사용자 입니다.",
				"result": {}
			}
			return Response(content, status=status.HTTP_404_NOT_FOUND)

		serializer = MemberSerializer(self.member)
		return Response(serializer.data)

	def put(self, request, id_member, *args, **kwargs):
		self.member = Member.objects.get(id_member=id_member)
		serializer = MemberReviseSerializer(self.member, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, *args, **kwargs):
		self.member.delete()
		content = {
			"message": "pk :" + request.id_member + " 삭제 완료",
			"result": {}
		}
		return Response(content, status=status.HTTP_204_NO_CONTENT)
