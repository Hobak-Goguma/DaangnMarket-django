from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sorl.thumbnail import get_thumbnail

from posts.models.product_model import Product
from posts.serializers.product_serializer import ProductSerializer, ProductTouchSerializer
from posts.models.posts_product_image_model import ProductImage


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, id_product):
    """
    제품 상세 조회, 업데이트, 삭제

    ---
    # parameter
        - s = 사진픽셀 크기 ex) 400x400
        - q = 사진품질 ex) 1~100 당근마켓은 82

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
        q = int(request.GET['q'])
        # TODO 데이터 가져올때, id_product_img기준으로 정렬(오름차순)
        Data = ProductImage.objects.filter(id_product=id_product)

        imageList = []
        imageDict = {}
        # TODO 'SERVER_PROTOCOL': 'HTTP/1.0', request.META['SERVER_PROTOCOL'] HTTP값으로 변환
        for i in range(Data.count()):
            imageDict['thum'] = request.META['HTTP_HOST'] + '/image' + get_thumbnail(Data[i].image, s, crop='center',
                                                                                     quality=q).url
            imageDict['origin'] = request.META['HTTP_HOST'] + '/image/media/' + str(Data[i].image)
            imageList.append(imageDict)
            content = serializer.data
            content['image'] = imageList
            return Response(content, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ProductTouchSerializer(product, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        content = {
            "message": "pk :" + id_product + " 삭제 완료",
            "result": {}
        }
        content = ""
        return Response(content, status=status.HTTP_204_NO_CONTENT)
