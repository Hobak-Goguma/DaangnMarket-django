from drf_yasg import openapi

# Manual Parameter
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

# Example
member_list_example = {
	    'name' : '김뚜시',
	    'nick_name' : 'ddusi',
	    'user_id' : 'ddusi',
	    'user_pw' : '1234',
	    'tel' : '010-0000-0000',
	    'birth' : '1994-03-30',
	    'email' : 'ddusi@kakao.com',
	    'gender' : 'MALE',
	    'cdate' : '',
	    'udate' : '2020-08-30 18:23:48.824951',
	    'last_data' : ''
	}

member_list_get_example = {
  "count": 3,
  "next": "http://localhost:8000/member?page=2&page_size=1",
  "previous": None,
  "results": [
    {
      "id_member": 1,
      "name": "김뚜띠",
      "nick_name": "동이",
      "user_id": "dduddi555",
      "user_pw": "password",
      "tel": "010-0000-0000",
      "birth": "2000-05-04",
      "email": "dduddi555@test.com",
      "gender": "MALE",
      "image": None,
      "cdate": "2020-08-24T01:25:27.560103",
      "udate": "2020-09-10T08:05:36.494970",
      "last_date": None
    }
  ]
}




# custom response schema
member_list_get_schema = openapi.Schema(
    'response',
    type=openapi.TYPE_OBJECT,
    properties={
    'count': openapi.Schema(type=openapi.TYPE_INTEGER, \
                           description='객체 갯수'),
    'next': openapi.Schema(type=openapi.TYPE_INTEGER, \
                           description='다음 페이지'),
    'previous': openapi.Schema(type=openapi.TYPE_INTEGER, \
                           description='이전 페이지'),
    'results': openapi.Schema(type=openapi.TYPE_OBJECT, \
                           properties=member_list_schema)
    },
    example=member_list_get_example
)