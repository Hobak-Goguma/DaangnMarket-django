from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from common.models.member_model import Member
from common.serializers.member_serializer import MemberReviseSerializer
from common.views.schema.member_detail_schema import member_detail_schema, member_detail_example, \
	member_detail_parameter


class MemberDetail(APIView):
	"""
	개별 멤버 수정, 삭제

	---
	멤버의 id_member를 통해 개별 수정, 삭제 합니다.
	"""
	permission_classes = [AllowAny]

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

	@swagger_auto_schema(manual_parameters=member_detail_parameter,
	        request_body=openapi.Schema(
			type=openapi.TYPE_OBJECT,
			properties=member_detail_schema,
			example=member_detail_example,
			required=['user_id']
			),
            operation_id='member_update',
			responses={
				200: 'Member Password Modification Successful.'
			})
	def put(self, request, id_member, *args, **kwargs):
		self.member = Member.objects.get(id_member=id_member)
		serializer = MemberReviseSerializer(self.member, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	@swagger_auto_schema(
			operation_id='member_delete',
			responses={
				204: 'Member delete succeeded.'
			})
	def delete(self, request, id_member, *args, **kwargs):
		self.member.delete()
		content = {
			"message": "pk :" + id_member + " 삭제 완료",
			"result": {}
		}
		return Response(content, status=status.HTTP_204_NO_CONTENT)
