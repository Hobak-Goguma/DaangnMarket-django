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
member_upload_file_delete = [id_member]

# Schema

# Example

# custom response schema
