from drf_yasg import openapi

member_touch_schema = {
            'name': openapi.Schema(type=openapi.TYPE_STRING, \
                description='회원 이름'),
            'nick_name': openapi.Schema(type=openapi.TYPE_STRING, \
                description='사용될 닉네임'),
            '   ser_id': openapi.Schema(type=openapi.TYPE_STRING, \
                description='회원 아이디 (유니크)'),
            '   ser_pw': openapi.Schema(type=openapi.TYPE_STRING, \
                description='회원 비밀번호'),
            '   el': openapi.Schema(type=openapi.TYPE_STRING, \
                description='전화번호 ex) 010-0000-0000'),
            '   irth': openapi.Schema(type=openapi.FORMAT_DATE, \
                description='생년월일 ex) 2002-05-09'),
            '   mail': openapi.Schema(type=openapi.TYPE_STRING, \
                description='이메일 ex) daangn@daangn.site'),
            '   ender': openapi.Schema(type=openapi.TYPE_STRING, \
                description='성별 MALE / FEMALE'),
            '   mage': openapi.Schema(type=openapi.TYPE_FILE, \
                description='프로필 사진 (갯수는 1개로 제한)'),
            '   date': openapi.Schema(type=openapi.FORMAT_DATETIME, \
                description='회원 가입일 ex) 2020-08-30 18:23:48.824951'),
            '   date': openapi.Schema(type=openapi.FORMAT_DATETIME, \
                description='회원 수정일 ex) 2020-08-31 16:30:37.808874'),
            '   ast_date': openapi.Schema(type=openapi.FORMAT_DATETIME, \
                description='마지막 로그인일 ex) 2020-09-08 02:26:55.248000'),
        }