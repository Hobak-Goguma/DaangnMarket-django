from drf_yasg import openapi

# Manual Parameter
image = openapi.Parameter(
    name='image',
    in_=openapi.IN_FORM,
    type=openapi.TYPE_FILE,
    description='This is company image(s)',
    required=True,
)

id_member = openapi.Parameter(
    name='id-member',
    in_=openapi.IN_HEADER,
    type=openapi.TYPE_INTEGER,
    description='This is a member pk',
    required=True,
)

company_upload_file_parameter = [id_member, image]
company_upload_file_delete = [id_member]

# Schema

# Example

# custom response schema
