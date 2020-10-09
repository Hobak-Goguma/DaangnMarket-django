from drf_yasg import openapi
# Manual Parameter
id_member = openapi.Parameter(
	name='id_member',
	in_=openapi.IN_BODY,
	type=openapi.TYPE_INTEGER,
	description='멤버 고유 ID',
	required=True,
)

wish_detail_parameters = [id_member, ]
# Schema
wish_detail_schema_delete = {
            'id_product': openapi.Schema(type=openapi.TYPE_INTEGER, \
              description='매물 고유 ID'),
        }

# Example
wish_detail_example_delete = {
	    'id_product': 7,
	}

# custom response schema
