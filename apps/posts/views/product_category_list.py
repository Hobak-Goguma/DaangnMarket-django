from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models.posts_category_code_model import CategoryCode


class ProductCategoryList(APIView):
	"""
	카테고리 조회
	---
	category : 1차 카테고리
	code : 2차 카테고리
	"""

	def get(self, request, *args, **kwargs):
		product_code = list(CategoryCode.objects.filter(category='PRODUCT').values_list('code', flat=True))
		promotion_code = list(CategoryCode.objects.filter(category='PROMOTION').values_list('code', flat=True))
		data = {
			"product_code": product_code,
			"promotion_code": promotion_code
		}
		return Response(data, status=status.HTTP_200_OK)
