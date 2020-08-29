from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from posts.models.product_model import Product
from posts.serializers.product_serializer import ProductSerializer


@api_view(['GET'])
def product_category(request):
    """
    제목에 검색어가 포함된 물건들 리스트
    """
    Search = request.GET['q']
    product = Product.objects.filter(code = Search)

    if not product:
        content = {
            "message" : "잘못된 카테고리 입니다.",
            "result" : {"입력한 검색어" : Search}
                }
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    else:
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
