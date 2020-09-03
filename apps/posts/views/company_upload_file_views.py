import os

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json

from posts.forms.company_upload_file_form import CompanyUploadFileForm
from posts.models.company_image_model import CompanyImage
from posts.models.company_model import Company


@api_view(('POST', 'DELETE'))
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
	# ImageFormSet = modelformset_factory(UploadFileModel, form=UploadFileForm, extra=10)

	if request.method == 'POST':
		id_member = request.headers['id-member']
		image_title: str = os.path.splitext(str(request.FILES['image']))[0]
		try:
			id_company: int = Company.objects.get(id_member=id_member).id_company
		except Company.DoesNotExist:
			content = {
				"message": "올바른 업체가 없습니다.",
				"result": request.POST['id_member']
			}
			Response(content, status=status.HTTP_404_NOT_FOUND)

		data = {
			"image_title": image_title,
			"id_company": id_company
		}
		form = CompanyUploadFileForm(data, request.FILES)
		if form.is_valid():
			form.save()
			content = {
				"message": "파일 업로드 완료",
				"result": {"image_title": image_title}
			}
			return Response(content, status=status.HTTP_200_OK)

		else:
			content = {
				"message": "데이터 형식이 맞지 않습니다.",
			}
			return Response(content, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		data = request.body.decode('utf-8')
		received_json_data = json.loads(data)
		id_member = received_json_data['id_member']
		q = CompanyImage.objects.filter(id_company__id_member=id_member).order_by('id').first()
		q_count = CompanyImage.objects.filter(id_company__id_member=id_member).count() - 1

		try:
			id: int = q.id
		except AttributeError:
			content = {
				"message": "더이상 업로드된 사진이 없습니다.",
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
