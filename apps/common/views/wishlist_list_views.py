from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from common.views.schema.wishlist_list_schema import wishlist_list_parameters, wishlist_list_schema_create, \
    wishlist_example_create

from posts.models.product_model import Product
from common.models.wishlist_model import Wishlist
from common.serializers.wish_list_serializer import WishlistSerializer


@swagger_auto_schema(
    method='get',
    responses={
         200: 'Success'
    }
)
@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties=wishlist_list_schema_create,
        example=wishlist_example_create,
        required=['addr']
    ),
    responses={
        201: 'Success',
        404: 'Bad request'
    }
)
@api_view(['GET', 'POST'])
def wishlist_list(request):
    """
    찜 리스트 조회, 생성 API

    ---
    찜리스트를 모두 보여주거나 새 찜을 추가합니다.
    """
    if request.method == 'GET':
        wishlist = Wishlist.objects.all()
        serializer = WishlistSerializer(wishlist, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WishlistSerializer(data=request.data)
        q = request.data
        try:
            product = Product.objects.get(id_product=q['id_product'])
        except Product.DoesNotExist:
            content = {
                "message": "없는 매물입니다.",
                "result": {}
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        try:
            # 자신이 등록한 상품인지 확인한다.
            product = Product.objects.get(id_product=q['id_product'], id_member=q['id_member'])
        except Product.DoesNotExist:
            # 이미 내가 등록한 찜리스트에 있는지 확인한다.
            try:
                wishlist = Wishlist.objects.get(id_product=q['id_product'], id_member=q['id_member'])
            except Wishlist.DoesNotExist:
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            content = {
                "message": "이미 찜리스트에 등록된 상품입니다.",
                "result": {}
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        content = {
            "message": "멤버 본인이 등록한 상품입니다.",
            "result": {}
        }
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
