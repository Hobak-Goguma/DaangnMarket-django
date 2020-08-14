from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from common.models.wishlist_model import Wishlist
from common.serializers.wish_list_serializer import WishlistSerializer


@api_view(['GET', 'DELETE'])
def wishlist_detail(request, id_member):
    """
    특정 유저의 찜리스트를 조회, 삭제 합니다.
    """
    wishlist = Wishlist.objects.filter(id_member = id_member)
    if wishlist.count() == 0:
        content = {
            "message" : "찜한 상품이 없습니다.",
            "result" : {}
                }
        return Response(content, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WishlistSerializer(wishlist, many=True)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        q = request.data
        qid_product = q['id_product']
        wishlist_delete = Wishlist.objects.filter(id_member = id_member).filter(id_product = qid_product)
        wishlist_delete.delete()
        content = {
            "message": "pk : " + str(qid_product) + " 삭제 완료",
            "result": {}
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)
