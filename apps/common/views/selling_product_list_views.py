from rest_framework.decorators import api_view
from rest_framework.response import Response

from posts.models.product_model import Product
from posts.serializers.product_serializer import ProductSerializer


@api_view(['GET'])
def selling_product_list(request, id_member):
    """
    특정 유저의 판매 상품 리스트를 조회합니다.
    """
    # objects.get은 단건을 조회하기 위한 용도이고, 없을 경우 DoesNotExist에러를 발생시킨다.
    # objects.filter는 여러 건의 객체를 조회하기 위한 용도이고, 없을 경우 빈 queryset을 리턴한다.
    # 즉, filter를 할 때 DoesNotExist Exception을 체크하는 것은 의미가 없다.
    product = Product.objects.filter(id_member = id_member)
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)