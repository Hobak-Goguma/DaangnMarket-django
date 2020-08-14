from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from posts.models.product_model import Product
from posts.serializers.product_serializer import ProductSerializer


@api_view(['GET'])
def product_search(request):
    """
    제목에 검색어가 포함된 물건들 리스트
    """

    # 디폴트 페이지네이션 사용
    paginator = PageNumberPagination()

    # 페이지 사이즈를 page_size라는 이름의 파라미터로 받을 거임
    paginator.page_size_query_param = "page_size"

    Search = request.GET['q']
    product = Product.objects.filter(name__contains = Search)

    if product.count() == 0:
        #검색 결과 없음.
        content = {
            "message" : "검색한 제품이 없습니다.",
            "result" : {"입력한 검색어" : Search}
                }
        return Response(content, status=status.HTTP_204_NO_CONTENT)

    # 페이지 적용된 쿼리셋
    paginated_product = paginator.paginate_queryset(product, request)

    # 페이지 파라미터 (page, page_size) 있을 경우
    # page_size 만 있을 경우 page=1 처럼 동작함
    # page만 있을 경우 아래 if문 안 탐
    if paginated_product is not None:
        serializers = ProductSerializer(paginated_product, many=True)
        return paginator.get_paginated_response(serializers.data)

    # 페이지 파라미터 없을 경우
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)
    # return HttpResponse(product)
