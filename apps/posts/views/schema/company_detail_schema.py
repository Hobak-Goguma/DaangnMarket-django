from drf_yasg import openapi

# Manual Parameter
id_member = openapi.Parameter(
    'id_member',
    openapi.IN_HEADER,
    description='This is a member id number',
    type=openapi.TYPE_STRING
)

s = openapi.Parameter(
    's',
    openapi.IN_QUERY,
    description='This is the size of images.',
    type=openapi.TYPE_STRING,
    required=True
)

company_detail_put_parameter = [id_member]
company_detail_get_parameter = [s]

# Schema
company_detail_schema = {
    'name': openapi.Schema(type=openapi.TYPE_STRING, description='업체 이름'),
    'addr': openapi.Schema(type=openapi.TYPE_STRING, description='업체 주소'),
    'tel': openapi.Schema(type=openapi.TYPE_STRING, description='업체 전화번호'),
    'info': openapi.Schema(type=openapi.TYPE_STRING, description='업체 설명'),
    'code': openapi.Schema(type=openapi.TYPE_STRING, description='업체 카테고리 코드'),
}
# Example
company_detail_example = {
    'name': '강아지나라',
    'addr': '가락본동',
    'tel': '02-000-000',
    'info': '애완용품점',
    'code': 'LOCAL_SHOP',
}
# custom response schema
