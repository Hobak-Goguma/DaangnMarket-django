from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sorl.thumbnail import get_thumbnail

from posts.models.posts_product_image_model import ProductImage


@api_view(('GET',))
def product_thumbnail(request, id_product):
    """
    물품 상세페이지의 썸네일을 리스트로 주는 API

    ---
    # 내용
        - s : 사진픽셀 크기 ex)500x500
        - q : 사진품질 0~100 ex)82 당근마켓 기본값
    """
    if request.method == 'GET':
        s = request.GET['s']
        q = int(request.GET['q'])
        Data = ProductImage.objects.filter(id_product=id_product)
        imageList=[]
        for i in range(Data.count()):
            imageList.append(request.META['HTTP_HOST'] + '/image' + get_thumbnail(Data[i].image, s, crop='center', quality=q).url)
        return Response(imageList, status=status.HTTP_200_OK)




# @api_view(('GET',))
# def productThumbnail(request, id_product):
#     if request.method == 'GET':
#         print("----------------1-------------------")
#         Data = UploadFileModel.objects.get(id_product=id_product)
#         print("----------------2-------------------")
#         # print(Data[0].image)
#         print("----------------2-1-----------------")
#         s = request.GET['s']
#         print("----------------3-------------------")
#         # print(get_thumbnail(Data[0].image, s, crop='center', quality=82))
#         return redirect('/image' + get_thumbnail(Data.image, s, crop='center', quality=82).url)



'''
# template 활용
@api_view(('GET',))
def productThumbnail(request, title):
    if request.method == 'GET':
        Data = UploadFileModel.objects.get(title=title)
        s = request.GET['s']
        return render(request, 'image/product.html', {"Data":Data} )
'''

