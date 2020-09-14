from drf_yasg import openapi

# Manual Parameter
user_id = openapi.Parameter(
    'user_id',
    openapi.IN_QUERY,
    description='확인 할 멤버 아이디',
    type=openapi.TYPE_STRING
)

member_overlap_parameter = [user_id]

nick_name = openapi.Parameter(
    'nick_name',
    openapi.IN_QUERY,
    description='확인 할 멤버 아이디',
    type=openapi.TYPE_STRING
)

nick_name_overlap_parameter = [nick_name]


# Schema


# Example


# custom response schema
