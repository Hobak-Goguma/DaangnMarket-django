from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, permissions

from posts.models.product_model import Product
from posts.serializers.product_serializer import ProductSearchSerializer


class ProductMyList(APIView):

	# authentication_classes = [authentication.TokenAuthentication]
	# permission_classes = [permissions.IsAdminUser]

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

		my_product = Product.objects.filter(id_member=id_member)
		serializer = ProductSearchSerializer(my_product, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
