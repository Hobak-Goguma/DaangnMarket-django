from drf_yasg import openapi

# Manual Parameter
id_member = openapi.Parameter(
    'id_member',
    openapi.IN_PATH,
    description='This is a member id number',
    type=openapi.TYPE_STRING
)

s_field = openapi.Parameter(
    's',
    openapi.IN_QUERY,
    description='This is the size of images.',
    type=openapi.TYPE_STRING
)

product_detail_put_parameter = [id_member]
product_detail_get_parameter = [id_member, s_field]

# Schema
product_detail_schema = {
    'name': openapi.Schema(type=openapi.TYPE_STRING, description='상품 이름'),
    'addr': openapi.Schema(type=openapi.TYPE_STRING, description='상품 주소'),
    'price': openapi.Schema(type=openapi.TYPE_INTEGER, description='상품 가격'),
    'info': openapi.Schema(type=openapi.TYPE_STRING, description='상품 설명'),
    'code': openapi.Schema(type=openapi.TYPE_STRING, description='상품 카테고리 코드'),
}
# Example
product_detail_example = {
    'name': '잘 달리는 자전거',
    'addr': '가락본동',
    'price': 13231,
    'info': '자전거가 날라가유 ~',
    'code': 'LOCAL_SHOP',
}
# custom response schema
