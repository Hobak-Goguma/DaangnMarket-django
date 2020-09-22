import os

from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.parsers import FormParser, MultiPartParser
from drf_yasg.utils import swagger_auto_schema
from posts.views.schema.product_upload_file_schema import product_upload_file_delete, product_upload_file_parameter

from posts.forms.product_upload_file_form import ProductUploadFileForm
from posts.models.posts_product_image_model import ProductImage
from posts.models.product_model import Product


@swagger_auto_schema(method='post',
                     manual_parameters=product_upload_file_parameter,
                     responses={
                         201: 'File Upload Successful.'
                     })
@swagger_auto_schema(method='delete',
                     manual_parameters=product_upload_file_delete,
                     responses={
                         204: 'File Deleted Successful.'
                     })
@api_view(('POST', 'DELETE'))
@parser_classes([FormParser, MultiPartParser])
def product_upload_file(request):
    """
	Product 사진 업로드 API

	---
	# 내용
		- image_title : 파일의 원본이름
		- id_product : Product 외래키
		- image : 업로드 할 이미지
	"""
    # 이미지 업로드 제한갯수 최대 10개 (try)
    # ImageFormSet = modelformset_factory(UploadFileModel, form=UploadFileForm, extra=10)

    if request.method == 'POST':
        id_member = request.headers['id-member']
        try:
            image_title: str = os.path.splitext(str(request.FILES['image']))[0]
        except KeyError:
            content = {
                "message": "데이터 형식이 맞지 않습니다.",
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        try:
            id_product: int = Product.objects.filter(id_member=id_member).get(
                id_product=request.POST['id_product']).id_product
        except Product.DoesNotExist:
            content = {
                "message": "올바른 상품이 없습니다.",
                "result": request.POST['id_product']
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        data = {
            "image_title": image_title,
            "id_product": id_product
        }
        form = ProductUploadFileForm(data, request.FILES)
        try:
            form.is_valid()
            form.save()
        except ValueError:
            content = {
                "message": "Allow up to 10 images.",
                "result": ProductImage.objects.filter(id_product=id_product).count()
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        content = {
            "message": "파일 업로드 완료",
            "result": {"image_title": image_title}
        }
        return Response(content, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        id_product = request.POST['id_product']
        q = ProductImage.objects.filter(id_product=id_product).order_by('id_product_img').first()
        q_count = ProductImage.objects.filter(id_product=id_product).count() - 1

        try:
            id: int = q.id_product_img
        except AttributeError:
            content = {
                "message": "더이상 업로드된 사진이 없습니다.",
                "result": {"id_company": id_product}
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        q.delete()
        content = {
            "message": "삭제 완료",
            "result": {
                "id": id,
                "image_count": q_count
            }
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)


'''
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return Response(status=status.HTTP_200_OK)
        # else:
        #     form = ModelFormWithFileField()
        #     return Response(status=status.HTTP_404_NOT_FOUND)
        # return Response(status=status.HTTP_404_NOT_FOUND)

        # return render(request, 'image/upload.html', {'form': form})
'''
