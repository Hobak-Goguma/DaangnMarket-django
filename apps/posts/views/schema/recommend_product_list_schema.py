from drf_yasg import openapi

# Manual Parameter
page_field = openapi.Parameter(
    'page',
    openapi.IN_QUERY,
    description='This is a page number.',
    type=openapi.TYPE_STRING
)
page_size_field = openapi.Parameter(
    'page_size',
    openapi.IN_QUERY,
    description='This is a page size.',
    type=openapi.TYPE_INTEGER
)

id_member_header = openapi.Parameter(
    'id-member',
    openapi.IN_HEADER,
    description="This is a member's pk",
    type=openapi.TYPE_INTEGER,
    requirement=False
)

recommend_product_list_parameter = [page_field, page_size_field, id_member_header]

# Schema

# Example

# custom response schema
