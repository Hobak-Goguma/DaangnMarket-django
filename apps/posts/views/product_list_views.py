from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.pagination import PageNumberPagination
from posts.views.schema.product_list_schema import product_list_parameter, product_list_schema_create, \
    product_list_example_create


from posts.models.product_model import Product
from posts.serializers.product_serializer import ProductSearchSerializer, ProductSerializer


@swagger_auto_schema(method='get',
                     tags=['product'],
                     manual_parameters=product_list_parameter,
                     responses={
                         200: '상품 조회 성공'
                     })
@swagger_auto_schema(method='post',
                     tags=['product'],
                     request_body=openapi.Schema(
                         type=openapi.TYPE_OBJECT,
                         properties=product_list_schema_create,
                         example=product_list_example_create,
                         required=['id_member', 'addr', 'name', 'tel', 'info', 'code']
                     ),
                     responses={
                         200: '상품 등록 성공'
                     })
@api_view(['GET', 'POST'])
def product_list(request):
    """
    상품을 모두 보여주거나 새 상품리스트를 만듭니다.

    ---
    # form/data OR json/data
        - id_product : seq key
        - id_member : 상품을 올린 member 외래키
        - name : 상품 제목
        - price : 상품 가격
        - info : 상품 내용
        - category : 상품 카테고리
        - views : 상품 조회수
        - state : '판매중' / '예약중' / '판매완료' 텍스트로
        - addr : 판매가 이루어질 장소 (동설정까지만 가능)
        - image : 리스트형식의 이미지 URLs
    """
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size_query_param = "page_size"
        product = Product.objects.all().order_by('-cdate')
        paginated_product = paginator.paginate_queryset(product, request)
        serializer = ProductSearchSerializer(paginated_product, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
