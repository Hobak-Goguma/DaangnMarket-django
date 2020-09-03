from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from common.models.member_model import Member
from common.serializers.member_serializer import MemberReviseSerializer


class MemberDetail(APIView):
	"""
	개별 유저 조회, 업데이트, 삭제
	---
	유저의 id_member를 통해 개별 조회, 업데이트, 삭제 합니다.
	"""
	def initial(self, request, id_member, *args, **kwargs):
		self.format_kwarg = self.get_format_suffix(**kwargs)
		neg = self.perform_content_negotiation(request)
		request.accepted_renderer, request.accepted_media_type = neg
		version, scheme = self.determine_version(request, *args, **kwargs)
		request.version, request.versioning_scheme = version, scheme
		self.perform_authentication(request)
		self.check_permissions(request)
		self.check_throttles(request)

		try:
			self.member = Member.objects.get(id_member=id_member)
		except Member.DoesNotExist:
			content = {
				"message": "없는 사용자 입니다.",
				"result": {}
			}
			return Response(content, status=status.HTTP_404_NOT_FOUND)

	# def get(self, request, *args, **kwargs):
	# 	serializer = MemberSerializer(self.member)
	# 	return Response(serializer.data)

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
