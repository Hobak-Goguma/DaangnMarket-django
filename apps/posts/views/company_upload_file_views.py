import os

from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.utils import json

from posts.forms.company_upload_file_form import CompanyUploadFileForm
from posts.models.company_image_model import CompanyImage
from posts.models.company_model import Company
from posts.views.schema.company_upload_file_schema import company_upload_file_delete, company_upload_file_parameter


@swagger_auto_schema(method='post',
                     manual_parameters=company_upload_file_parameter,
                     responses={
                         201: 'File Upload Successful.'
                     })
@swagger_auto_schema(method='delete',
                     manual_parameters=company_upload_file_delete,
                     responses={
                         204: 'File Deleted Successful.'
                     })
@api_view(('POST', 'DELETE'))
@parser_classes([FormParser, MultiPartParser])
def company_upload_file(request):
    """
	Product 사진 업로드 API

	---
	# 내용
		- image_title : 파일의 원본이름
		- id_company : Company 외래키
		- image : 업로드 할 이미지
	"""
    # 이미지 업로드 제한갯수 최대 10개 (try)
    # ImageFormSet = modelformset_factory(CompanyImage, form=CompanyUploadFileForm, extra=10)

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
            id_company: int = Company.objects.get(id_member=id_member).id_company
        except Company.DoesNotExist:
            content = {
                "message": "올바른 업체가 없습니다.",
                "result": request.headers['id-member']
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        data = {
            "image_title": image_title,
            "id_company": id_company
        }
        form = CompanyUploadFileForm(data, request.FILES)
        try:
            form.is_valid()
            form.save()

        except ValueError:
            content = {
                "message": "Allow up to 10 images.",
                "result": CompanyImage.objects.filter(id_company=id_company).count()
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        content = {
            "message": "파일 업로드 완료",
            "result": {"image_title": image_title}
        }
        return Response(content, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        id_member = request.headers['id_member']
        q = CompanyImage.objects.filter(id_company__id_member=id_member).order_by('id').first()
        q_count = CompanyImage.objects.filter(id_company__id_member=id_member).count() - 1

        try:
            id: int = q.id
        except AttributeError:
            content = {
                "message": "더 이상 업로드된 사진이 없습니다.",
                "result": {"id_company": id_member}
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
