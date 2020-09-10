from drf_yasg import openapi

# Manual Parameter

# Schema
member_login_schema = {
            'user_id': openapi.Schema(type=openapi.TYPE_STRING, \
              description='회원 아이디 (유니크)'),
            'user_pw': openapi.Schema(type=openapi.TYPE_STRING, \
              description='회원 비밀번호'),
        }

# Example
member_login_example = {
		'user_id' : 'ddusi',
		'user_pw' : '1234',
	}

member_login_post_example = {
  "id_member": 1,
  "user_id": "ddusi",
  "name": "김뚜시",
  "nick_name": "ddusi",
  "tel": "010-0000-0000",
  "last_date": "2020-08-24T01:25:27.560103"
}

# custom response schema
member_login_post_schema = openapi.Schema(
    'response',
    type=openapi.TYPE_OBJECT,
    properties={
    'id_member': openapi.Schema(type=openapi.TYPE_INTEGER, \
                           description='멤버 고유 id'),
    'user_id': openapi.Schema(type=openapi.TYPE_STRING, \
                           description='회원 아이디 (유니크)'),
    'name': openapi.Schema(type=openapi.TYPE_STRING, \
                           description='회원 이름'),
    'nick_name': openapi.Schema(type=openapi.TYPE_STRING, \
                           description='사용될 닉네임'),
    'tel': openapi.Schema(type=openapi.TYPE_STRING, \
                           description='전화번호 ex) 010-0000-0000'),
    'last_date': openapi.Schema(type=openapi.FORMAT_DATETIME, \
                           description='마지막 로그인일 ex) 2020-09-08 02:26:55.248000'),
    'image': openapi.Schema(type=openapi.TYPE_FILE, \
                           description='프로필 사진 (갯수는 1개로 제한)'),
    },
    # example=member_list_get_example
)