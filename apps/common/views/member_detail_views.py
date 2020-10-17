from django.conf import settings
from django.contrib.auth.models import User
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from jwt import decode
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from common.models.member_model import Member
from common.views.schema.member_detail_schema import member_detail_schema, member_detail_example, \
	member_detail_parameter


class MemberDetail(APIView):
	"""
	개별 멤버 수정, 삭제

	---
	멤버의 id_member를 통해 개별 수정, 삭제 합니다.
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

	@swagger_auto_schema(manual_paSrameters=member_detail_parameter,
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
		# serializer = MemberReviseSerializer(self.member, data=request.data)
		# if serializer.is_valid():
		# 	serializer.save()
		# 	return Response(serializer.data)
		user_token = request.headers['Authorization'].split(' ')[1]
		token_decoded = decode(user_token, settings.SECRET_KEY, algorithms=['HS256'])

		if id_member != token_decoded['user_id']:
			return Response(status=status.HTTP_401_UNAUTHORIZED)

		try:
			self.member = Member.objects.get(auth=token_decoded['user_id'])
			self.user = User.objects.get(id=token_decoded['user_id'])
		except Member.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		self.user.set_password(request.data['user_pw'])
		self.user.save()
		self.member.user_pw = self.user.password
		self.member.save()

		return Response(status=status.HTTP_202_ACCEPTED)

	@swagger_auto_schema(
		operation_id='member_delete',
		responses={
			204: 'Member delete succeeded.'
		})
	def delete(self, request, id_member, *args, **kwargs):
		user_token = request.headers['Authorization'].split(' ')[1]
		token_decoded = decode(user_token, settings.SECRET_KEY, algorithms=['HS256'])

		if id_member != token_decoded['user_id']:
			return Response(status=status.HTTP_401_UNAUTHORIZED)

		try:
			self.member = Member.objects.get(auth=token_decoded['user_id'])
			self.user = User.objects.get(id=token_decoded['user_id'])
		except Member.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		self.member.delete()
		self.user.delete()
		content = {
			"message": "pk :" + str(id_member) + " 삭제 완료",
			"result": {}
		}
		return Response(content, status=status.HTTP_204_NO_CONTENT)
