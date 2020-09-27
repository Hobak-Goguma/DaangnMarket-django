from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sorl.thumbnail import get_thumbnail
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from posts.views.schema.product_detail_schema import product_detail_example, product_detail_schema, \
    product_detail_get_parameter, product_detail_put_parameter

from posts.models.posts_product_image_model import ProductImage
from posts.models.product_model import Product
from posts.serializers.product_serializer import ProductSerializer, ProductTouchSerializer


@swagger_auto_schema(method='put',
                     tags=['product'],
                     manual_parameter=product_detail_put_parameter,
                     request_body=openapi.Schema(
                         type=openapi.TYPE_OBJECT,
                         properties=product_detail_schema,
                         example=product_detail_example,
                         required=['name', 'addr', 'tel', 'info', 'code']
                     ),
                     responses={
                         200: 'Update Successfully'
                     })
@swagger_auto_schema(method='get',
                     tags=['product'],
                     manual_parameters=product_detail_get_parameter,
                     responses={
                         200: 'Detail Successfully'
                     })
@swagger_auto_schema(method='delete',
                     tags=['product'],
                     responses={
                         204: 'Delete Successfully'
                     })
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, id_product):
    """
	제품 상세 조회, 업데이트, 삭제

	---
	# parameter
		- s = 사진픽셀 크기 ex) 400x400

	# 수정가능 목록 form/data OR json/data
		- name : 상품 제목
		- price : 상품 가격
		- info : 상품 내용
		- category : 상품 카테고리
		- addr : 판매가 이루어질 장소 (동설정까지만 가능)

	# 내용
		image : {
		- thum : 사진 썸네일
		- origin : 사진 원본
		}
	"""

    try:
        product = Product.objects.get(id_product=id_product)
    except Product.DoesNotExist:
        content = {
            "message": "없는 물품리스트 입니다.",
            "result": {}
        }
        return Response(content, status=status.HTTP_404_NOT_FOUND)
    # except Product.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # product = Product.objects.get(id_product=id_product)
        product.views += 1
        product.save()
        serializer = ProductSerializer(product)

        s = request.GET['s']
        image = ProductImage.objects.filter(id_product=id_product).order_by('id_product_img')
        imageList = []
        data = serializer.data
        for i in range(image.count()):
            imageDict = {}
            imageDict['thum'] = request.META['HTTP_HOST'] + '/posts' + get_thumbnail(image[i].image, s, crop='center',
                                                                                     quality=82).url
            imageDict['origin'] = request.META['HTTP_HOST'] + '/posts/media/' + str(image[i].image)
            imageList.append(imageDict)
        data['image'] = imageList
        return Response(data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ProductTouchSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        content = {
            "message": "pk :" + str(id_product) + " 삭제 완료",
            "result": {}
        }
        content = ""
        return Response(content, status=status.HTTP_204_NO_CONTENT)
