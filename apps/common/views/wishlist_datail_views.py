from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from common.models.wishlist_model import Wishlist
from common.serializers.wish_list_serializer import WishlistSerializer
from common.views.schema.wishlist_detail_schema import wish_detail_example_delete, wish_detail_parameters ,wish_detail_schema_delete


@swagger_auto_schema(
    method='get',
    responses={
         200: 'Success'
    }
)
@swagger_auto_schema(
    method='delete',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties=wish_detail_schema_delete,
        example=wish_detail_example_delete,
        required=['addr']
    ),
    responses={
        204: 'Success',
        404: 'Does Not exist Wishlist'
    }
)
@api_view(['GET', 'DELETE'])
def wishlist_detail(request, id_member):
    """
    특정 유저의 찜 조회, 삭제 API

    ---
    특정 유저의 찜리스트를 조회, 삭제 합니다.
    """
    wishlist = Wishlist.objects.filter(id_member=id_member)
    if wishlist.count() == 0:
        content = {
            "message": "찜한 상품이 없습니다.",
            "result": {}
                }
        return Response(content, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WishlistSerializer(wishlist, many=True)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        wishlist_delete = Wishlist.objects.filter(id_member=id_member).filter(id_product=request.data['id_product'])
        wishlist_delete.delete()
        content = {
            "message": "pk : " + str(request.data['id_product']) + " 삭제 완료",
            "result": {}
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)
