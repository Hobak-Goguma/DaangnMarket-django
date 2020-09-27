from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework import authentication, permissions
from drf_yasg.utils import swagger_auto_schema
from posts.views.schema.product_my_list_schema import product_my_list_parameter

from posts.models.product_model import Product
from posts.serializers.product_serializer import ProductSearchSerializer


class ProductMyList(APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    @swagger_auto_schema(manual_parameters=product_my_list_parameter,
                         tags=['product'],
                         operation_id='product_my_list',
                         responses={
                             200: 'Member Password Modification Successful.'
                         })
    def get(self, request, format=None):
        """
		내 제품 상세 조회, 업데이트, 삭제
		"""
        try:
            id_member = request.headers['id-member']
        except KeyError:
            content = {
                "message": "올바른 ID값이 아닙니다.",
                "result": {}
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        paginator = PageNumberPagination()

        paginator.page_size_query_param = "page_size"

        my_product = Product.objects.filter(id_member=id_member).order_by('-cdate')
        paginated_my_product = paginator.paginate_queryset(my_product, request)

        if paginated_my_product is not None:
            serializers = ProductSearchSerializer(paginated_my_product, many=True, context={'request': request})
            return paginator.get_paginated_response(serializers.data)

        serializer = ProductSearchSerializer(my_product, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
