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

company_list_parameter = [page_field, page_size_field]

# Schema
company_list_schema_create = {
    'id_member': openapi.Schema(type=openapi.TYPE_INTEGER, \
                                description='멤버 고유 ID'),
    'name': openapi.Schema(type=openapi.TYPE_STRING, \
                           description='업체 이름'),
    'addr': openapi.Schema(type=openapi.TYPE_STRING, \
                           description='업체 설정 주소 (주소는 1개가지 설정 가능)'),
    'tel': openapi.Schema(type=openapi.TYPE_STRING, \
                          description='업체 전화번호'),
    'info': openapi.Schema(type=openapi.TYPE_STRING, \
                           description='업체 설명'),
    'code': openapi.Schema(type=openapi.TYPE_STRING, \
                           description='업체 카테고리 코드 ([유효성 검사] 허용된 코드 : LOCAL_SHOP)'),

}

# Example
company_list_example_create = {
    'id_member': '1',
    'name': '별나라방앗간',
    'addr': '신림동',
    'tel': '02-0000-0000',
    'info': '떡 만들어요',
    'code': 'LOCAL_SHOP'
}

# custom response schema
