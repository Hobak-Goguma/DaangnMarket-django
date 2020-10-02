from rest_framework_simplejwt.authentication import JWTAuthentication as j


def helper_jwt_get_user(self, request):
	"""
	www_authenticate_realm = 'api'
	HelperJwtGetUser(self, request)
	이런식으로 사용하여 토큰에서 user정보를 찾아내는 uitll입니다.
	"""
	JWToken_user = j.get_user(self, j.get_validated_token(self, request.headers['Authorization'].split(' ')[1]))
	return JWToken_user
