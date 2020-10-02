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
id_member = openapi.Parameter(
    'id-member',
    openapi.IN_HEADER,
    description='This is a member id number',
    type=openapi.TYPE_INTEGER
)


product_my_list_parameter = [page_field, page_size_field, id_member]

# Schema


# Example


# custom response schema
