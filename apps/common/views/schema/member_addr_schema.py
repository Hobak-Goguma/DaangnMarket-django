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
              description='주소기준의 거리반경 (0, 2, 5, 10, 15 단위 : km)'),
        }

# Example
member_addr_example_create = {
	    'id_member': '1',
	    'addr': '신림동',
	}
member_addr_example = {
	    'addr': '신림동'
	}
member_addr_example_update = {
	    'addr': '신림동',
		'distance': 2
	}

# custom response schema
