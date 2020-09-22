from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from django.utils import timezone, dateformat
from rest_framework.pagination import PageNumberPagination

from posts.models.product_model import Product
from posts.serializers.product_serializer import ProductSearchSerializer
from common.models.member_model import Member
from common.models.member_addr_model import Memberaddr
from common.models.nearby_Location_model import NearbyLocation


class Pagination(PageNumberPagination):
    page_query_param = 'page'
    page_size_query_param = 'page_size'


class RecommendProductListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(cdate__year=timezone.now().year,
                                      cdate__month=timezone.now().month,
                                      cdate__day=timezone.now().day).order_by('-views',)
    serializer_class = ProductSearchSerializer
    pagination_class = Pagination

    def list(self, request):
        if 'id-member' not in request.headers:
            page = self.paginate_queryset(self.queryset)
            serializer = ProductSearchSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        id_member = request.headers['id-member']
        try:
            Member.objects.get(id_member=id_member)
        except Member.DoesNotExist:
            content = {
                "message": "없는 사용자입니다.",
                "result": {}
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        try:
            member_addr = Memberaddr.objects.filter(id_member=id_member).get(select='Y')
            addr = member_addr.addr
            dis = member_addr.distance
        # 설정된 주소가 없을
        except Memberaddr.DoesNotExist:
            content = {
                "message": "설정된 주소가 없습니다. 주소를 설정해 주세요.",
                "result": {}
                    }
            return Response(content,status=status.HTTP_204_NO_CONTENT)
        nearby_dong_list = list(NearbyLocation.objects.filter(dong=addr).filter(distance=dis).values_list('nearby_dong', flat=True))
        recommend_product_list = self.queryset.filter(addr__in=nearby_dong_list)
        page = self.paginate_queryset(recommend_product_list)
        serializer = ProductSearchSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)
