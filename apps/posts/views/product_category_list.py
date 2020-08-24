from posts.models.posts_category_code_models import CategoryCode
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.serializers.product_serializer import ProductCategoryCode


class ProductCategoryList(APIView):
	"""
	카테고리 조회
	---
	category : 1차 카테고리
	code : 2차 카테고리
	"""

	def get(self, request, *args, **kwargs):
		category = CategoryCode.objects.all()
		serializer = ProductCategoryCode(category, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)