from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from posts.models.posts_category_code_model import CategoryCode


class ProductCategoryList(APIView):
    @swagger_auto_schema(operation_id='product_my_list',
                         tags=['product'],
                         responses={
                             200: 'Success'
                         })
    def get(self, request, *args, **kwargs):
        """
        카테고리 조회 API

        ---
        category : 1차 카테고리
        code : 2차 카테고리
        """
        product_code = list(CategoryCode.objects.filter(category='PRODUCT').values_list('code', flat=True))
        promotion_code = list(CategoryCode.objects.filter(category='PROMOTION').values_list('code', flat=True))
        data = {
            "category": [
                {
                    "product": product_code,
                    "promotion": promotion_code
                }
            ]
        }
        return Response(data, status=status.HTTP_200_OK)
