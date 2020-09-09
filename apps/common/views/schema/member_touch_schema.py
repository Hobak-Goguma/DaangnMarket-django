from drf_yasg import openapi

# Manual Parameter

# Schema
member_touch_schema = {
            'nick_name': openapi.Schema(type=openapi.TYPE_STRING, \
              description='사용될 닉네임'),
            'tel': openapi.Schema(type=openapi.TYPE_STRING, \
              description='전화번호 ex) 010-0000-0000'),
            'birth': openapi.Schema(type=openapi.FORMAT_DATE, \
              description='생년월일 ex) 2002-05-09'),
            'email': openapi.Schema(type=openapi.TYPE_STRING, \
              description='이메일 ex) daangn@daangn.site'),
            'gender': openapi.Schema(type=openapi.TYPE_STRING, \
              description='성별 MALE / FEMALE'),
        }