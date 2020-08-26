import json

from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from common.models.member_model import Member
from common.serializers.login_serializer import LoginSerializer


@api_view(['POST'])
def member_login(request):
    """
    멤버 테이블 로그인
    """
    if request.method == 'POST':
        try:
            Data = json.loads(request.body)
            user_id = Data['user_id']
            user_pw = Data['user_pw']
            member = Member.objects.get(user_id = user_id, user_pw = user_pw)

        except Member.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        member.last_date = timezone.now()
        member.save()

        serializer = LoginSerializer(member)
        return Response(serializer.data)
    # if request.method == 'POST':
    #     serializer = LoginSerializer(member, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response(serializer.data)


    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)