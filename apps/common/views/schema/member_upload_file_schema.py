from drf_yasg import openapi

# Manual Parameter
image = openapi.Parameter(
	name='image',
	in_=openapi.IN_FORM,
    type=openapi.TYPE_FILE,
    description='멤버 프로필 이미지',
	required=True,
)

id_member = openapi.Parameter(
	name='id_member',
	in_=openapi.IN_FORM,
	type=openapi.TYPE_INTEGER,
	description='멤버 고유 ID',
	required=True,
)

member_upload_file_parameter = [id_member, image]
member_upload_file_json = [id_member]

# Schema
member_upload_file_schema = {
            'id_member': openapi.Schema(type=openapi.TYPE_INTEGER, \
              description='멤버 고유 ID'),
        }

# Example
member_upload_file_example = {
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

member_upload_file_get_example = {
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
member_upload_file_get_schema = openapi.Schema(
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
                           properties=member_upload_file_schema)
    },
    example=member_upload_file_get_example
)