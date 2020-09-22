from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from posts.views.schema.company_list_schema import company_list_parameter, company_list_schema_create, \
    company_list_example_create
from drf_yasg import openapi
from rest_framework.pagination import PageNumberPagination

from posts.models.company_model import Company
from posts.serializers.company_serializer import CompanySerializer, CompanySearchSerializer


@swagger_auto_schema(method='get',
                     manual_parameters=company_list_parameter,
                     responses={
                         200: '동네 업체 조회 성공'
                     })
@swagger_auto_schema(method='post',
                     request_body=openapi.Schema(
                         type=openapi.TYPE_OBJECT,
                         properties=company_list_schema_create,
                         example=company_list_example_create,
                         required=['id_member', 'addr', 'name', 'tel', 'info', 'code']
                     ),
                     responses={
                         200: '동네 업체 등록 성공'
                     })
@api_view(['GET', 'POST'])
def company_list(request):
    """
    업체리스트를 모두 보여주거나 새 업체리스트를 만듭니다.
    """
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size_query_param = "page_size"
        queryset = Company.objects.all().order_by('-cdate')
        paginated_company = paginator.paginate_queryset(queryset, request)
        serializer = CompanySearchSerializer(paginated_company, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
