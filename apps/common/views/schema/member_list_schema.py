from drf_yasg import openapi

# manual parameter
page_field = openapi.Parameter(
    'page',
    openapi.IN_QUERY,
    description='this is a page number',
    type=openapi.TYPE_STRING
)
page_size_field = openapi.Parameter(
    'page_size',
    openapi.IN_QUERY,
    description='this is a page size',
    type=openapi.TYPE_INTEGER
)

member_list_parameter = [page_field, page_size_field]

# Schema
member_list_schema = {
            'name': openapi.Schema(type=openapi.TYPE_STRING, \
              description='회원 이름'),
            'nick_name': openapi.Schema(type=openapi.TYPE_STRING, \
              description='사용될 닉네임'),
            'user_id': openapi.Schema(type=openapi.TYPE_STRING, \
              description='회원 아이디 (유니크)'),
            'user_pw': openapi.Schema(type=openapi.TYPE_STRING, \
              description='회원 비밀번호'),
            'tel': openapi.Schema(type=openapi.TYPE_STRING, \
              description='전화번호 ex) 010-0000-0000'),
            'birth': openapi.Schema(type=openapi.FORMAT_DATE, \
              description='생년월일 ex) 2002-05-09'),
            'email': openapi.Schema(type=openapi.TYPE_STRING, \
              description='이메일 ex) daangn@daangn.site'),
            'gender': openapi.Schema(type=openapi.TYPE_STRING, \
              description='성별 MALE / FEMALE'),
            'image': openapi.Schema(type=openapi.TYPE_FILE, \
              description='프로필 사진 (갯수는 1개로 제한)'),
            'cdate': openapi.Schema(type=openapi.FORMAT_DATETIME, \
              description='회원 가입일 ex) 2020-08-30 18:23:48.824951'),
            'udate': openapi.Schema(type=openapi.FORMAT_DATETIME, \
              description='회원 수정일 ex) 2020-08-31 16:30:37.808874'),
            'last_date': openapi.Schema(type=openapi.FORMAT_DATETIME, \
              description='마지막 로그인일 ex) 2020-09-08 02:26:55.248000'),
        }