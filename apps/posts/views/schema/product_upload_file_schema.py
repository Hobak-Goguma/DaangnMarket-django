from drf_yasg import openapi

# Manual Parameter
image = openapi.Parameter(
    name='image',
    in_=openapi.IN_FORM,
    type=openapi.TYPE_FILE,
    description='This is product image(s)',
    required=True,
)

id_member = openapi.Parameter(
    name='id-member',
    in_=openapi.IN_HEADER,
    type=openapi.TYPE_INTEGER,
    description='This is a member pk',
    required=True,
)

id_product = openapi.Parameter(
    name='id_product',
    in_=openapi.IN_FORM,
    type=openapi.TYPE_INTEGER,
    description='This is a product pk',
    required=True,
)

product_upload_file_parameter = [id_member, image, id_product]
product_upload_file_delete = [id_product]

# Schema

# custom response schema
