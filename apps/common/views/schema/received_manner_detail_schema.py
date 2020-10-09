from drf_yasg import openapi

# Manual Parameter
id_member = openapi.Parameter(
                'id-member',
                openapi.IN_HEADER,
                description='member pk',
                type=openapi.TYPE_STRING
            )
received_manner_parameter = [id_member, ]
# Schema
received_manner_schema = {
    'id_member': openapi.Schema(type=openapi.TYPE_INTEGER,
                                description='회원 pk'),
    'score': openapi.Schema(type=openapi.TYPE_INTEGER,
                            description='매너온도 점수'),
    'cdate': openapi.Schema(type=openapi.FORMAT_DATETIME,
                            description='생성일 ex) 2020-08-30 18:23:48.824951'),
    'udate': openapi.Schema(type=openapi.FORMAT_DATETIME,
                            description='수정일 ex) 2020-08-31 16:30:37.8874'),
}

# Example
received_manner_example = {
    'score': 36.5,
}

# custom response schema
