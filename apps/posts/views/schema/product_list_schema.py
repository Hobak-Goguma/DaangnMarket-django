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


product_list_parameter = [page_field, page_size_field]

# Schema
product_list_schema_create = {
    'id_member': openapi.Schema(type=openapi.TYPE_INTEGER, \
                                description='멤버 고유 ID'),
    'name': openapi.Schema(type=openapi.TYPE_STRING, \
                           description='상품 이름'),
    'price': openapi.Schema(type=openapi.TYPE_INTEGER, \
                           description='상품 가격'),
    'addr': openapi.Schema(type=openapi.TYPE_STRING, \
                           description='상품 설정 주소 (주소는 1개가지 설정 가능)'),
    'info': openapi.Schema(type=openapi.TYPE_STRING, \
                           description='상품 설명'),
    'code': openapi.Schema(type=openapi.TYPE_STRING, \
                           description='상품 카테고리 코드 ([유효성 검사] 허용된 코드 : LOCAL_SHOP)'),

}

# Example
product_list_example_create = {
    'id_member': '1',
    'name': '자전거',
    'addr': '가락1동',
    'price': 23100,
    'info': '3번 탔어요',
    'code': 'SPORTS'
}

# custom response schema
