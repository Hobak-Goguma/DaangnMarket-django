from drf_yasg import openapi

# Manual Parameter
addr = openapi.Parameter(
	name='addr',
	in_=openapi.IN_BODY,
    type=openapi.TYPE_FILE,
    description='멤버 프로필 이미지',
	required=True,
)

id_member = openapi.Parameter(
	name='id_member',
	in_=openapi.IN_BODY,
	type=openapi.TYPE_INTEGER,
	description='멤버 고유 ID',
	required=True,
)

member_addr_parameter = [id_member, addr]

# Schema
member_addr_schema_create = {
            'id_member': openapi.Schema(type=openapi.TYPE_INTEGER, \
              description='멤버 고유 ID'),
            'addr': openapi.Schema(type=openapi.TYPE_STRING, \
              description='멤버 설정 주소 (주소는 2개가지 설정 가능)'),
        }

member_addr_schema = {
            'addr': openapi.Schema(type=openapi.TYPE_STRING, \
              description='멤버 설정 주소 (주소는 2개가지 설정 가능)'),
        }

member_addr_schema_update = {
            'addr': openapi.Schema(type=openapi.TYPE_STRING, \
              description='멤버 설정 주소 (주소는 2개가지 설정 가능)'),
            'dis': openapi.Schema(type=openapi.TYPE_INTEGER, \
              description='주소기준의 거리반경 (0, 2, 5, 10, 15)'),
        }

# Example
member_addr_example_create = {
	    'id_member' : '1',
	    'addr' : '신림동',
	}
member_addr_example = {
	    'addr' : '신림동'
	}
member_addr_example_update = {
	    'addr' : '신림동',
		'dis' : 2
	}

member_addr_get_example = {
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
member_addr_get_schema = openapi.Schema(
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
                           properties=member_addr_schema)
    },
    example=member_addr_get_example
)