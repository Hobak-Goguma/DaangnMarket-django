from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from common.models.member_model import Member
from common.serializers.member_serializer import MemberSerializer
from common.views.schema.member_list_schema import member_list_schema, member_list_parameter, member_list_example, \
	member_list_get_schema


class MemberListView(APIView):
	"""
	멤버 리스트 조회, 생성 API

	---
	"""
	permission_classes = [AllowAny]

	@swagger_auto_schema(manual_parameters=member_list_parameter,
	                     responses={200: member_list_get_schema}
	                     )
	def get(self, request, format=None):
		paginator = PageNumberPagination()
		paginator.page_size_query_param = "page_size"

		queryset = Member.objects.all()
		queryset_paginate = paginator.paginate_queryset(queryset, request)
		serializer = MemberSerializer(queryset_paginate, many=True, context={'request': request})
		return paginator.get_paginated_response(serializer.data)

	@swagger_auto_schema(request_body=openapi.Schema(
		type=openapi.TYPE_OBJECT,
		properties=member_list_schema,
		example=member_list_example,
		required=['name', 'user_id', 'user_pw', 'nick_name', 'tel', 'cdate']
	),
		responses={
			201: 'Successfully created new members.'
		})
	def post(self, request, format=None):
		serializer = MemberSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
