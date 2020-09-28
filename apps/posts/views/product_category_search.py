from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.pagination import PageNumberPagination

from posts.models.product_model import Product
from posts.models.posts_category_code_model import CategoryCode
from posts.serializers.product_serializer import ProductSerializer
from posts.views.schema.product_category_search_schema import product_search_category_parameter


@swagger_auto_schema(method='get',
                     tags=['product'],
                     manual_parameters=product_search_category_parameter,
                     responses={
                         200: '성공',
                         404: '잘못된 카테고리'
                     })
@api_view(['GET'])
def product_category_search(request):
    """
    카테고리로 매물 검색 API

    ---
    제목에 검색어가 포함된 물건들 리스트
    """
    try:
        q = CategoryCode.objects.filter(code=request.GET['q'])
    except CategoryCode.DoesNotExist:
        content = {
            "message": "잘못된 카테고리 입니다.",
            "result": {"입력한 검색어": request.GET['q']}
        }
        return Response(content, status=status.HTTP_400_BAD_REQUESTS)

    paginator = PageNumberPagination()
    paginator.page_size_query_param = "page_size"
    Search = request.GET['q']
    product = Product.objects.filter(code=Search)

    paginated_product = paginator.paginate_queryset(product, request)
    serializer = ProductSerializer(paginated_product, many=True)
    return paginator.get_paginated_response(serializer.data)
