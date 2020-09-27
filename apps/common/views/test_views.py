from rest_framework.response import Response
from rest_framework.views import APIView

from common.helper.helper_jwt_get_user import helper_jwt_get_user


class TestView(APIView):
	"""
	테스트용 API
	---

	"""
	www_authenticate_realm = 'api'

	def post(self, request):
		# JWToken_user = j.get_user(self, j.get_validated_token(self, request.headers['Authorization'].split(' ')[1]))
		# print(j.get_header(self, request))
		# print(j.get_raw_token(self, j.get_header(self, request)))
		# print(j.get_validated_token(self, j.get_raw_token(self, j.get_header(self, request))))
		# print(type(j.get_validated_token(self, j.get_raw_token(self, j.get_header(self, request)))))
		print(helper_jwt_get_user(self, request))

		return Response()
