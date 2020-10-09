from drf_yasg import openapi

# Manual Parameter
id_member = openapi.Parameter(
	name='id_member',
	in_=openapi.IN_BODY,
	type=openapi.TYPE_INTEGER,
	description='멤버 고유 ID',
	required=True,
)

wishlist_list_parameters = [id_member, ]
# Schema
wishlist_list_schema_create = {
            'id_product': openapi.Schema(type=openapi.TYPE_INTEGER, \
              description='매물 고유 ID'),
            'id_member': openapi.Schema(type=openapi.TYPE_STRING, \
              description='멤버 고유 ID'),
        }

# Example
wishlist_example_create = {
	    'id_product': 7,
	    'id_member': 1,
	}

# custom response schema
