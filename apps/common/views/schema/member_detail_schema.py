from drf_yasg import openapi

# Manual Parameter
id_member = openapi.Parameter(
    'id_member',
    openapi.IN_PATH,
    description='this is a member id number',
    type=openapi.TYPE_STRING
)

member_detail_parameter = [id_member]

# Schema
member_detail_schema = {
            'user_pw': openapi.Schema(type=openapi.TYPE_STRING, \
              description='회원 비밀번호'),
            }

# Example
member_detail_example = {
	    'user_pw' : 'password',
	}