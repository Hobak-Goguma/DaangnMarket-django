from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from posts.models.product_model import Product
from posts.serializers.product_serializer import ProductSearchSerializer


@api_view(['GET'])
def test(request):
    """
    테스트용 api
    """
    if request.method == 'GET':
        product = Product.objects.filter(name__contains = '자전거')
        serializer = ProductSearchSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # if request.method == 'GET':
    #     product = ProductImage.objects.filter(id_product=44).order_by('id_product_img')
    #     print('=========================================')
    #     print(product)
    #     serializer = ProductImageSerializer(product, many=True)
    #     # print(serializer)
    #     return Response(serializer.data, status=status.HTTP_200_OK)