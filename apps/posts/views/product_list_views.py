from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from posts.models.product_model import Product
from posts.serializers.product_serializer import ProductSearchSerializer, ProductSerializer


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
        product = Product.objects.all()
        serializer = ProductSearchSerializer(product, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
