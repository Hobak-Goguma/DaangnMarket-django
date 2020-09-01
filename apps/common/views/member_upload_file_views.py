import os

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json

from common.forms.member_upload_file_form import MemberUploadFileForm
from common.models.member_model import Member


@api_view(('POST', 'DELETE'))
def member_upload_file(request):
	"""
	Product 사진 업로드 API

	---
	# 내용
		- title : 저장 할 파일이름
		- id_product : Product 외래키
		- image : 업로드 할 이미지
	"""
	# 이미지 업로드 제한갯수 최대 10개 (try)
	# ImageFormSet = modelformset_factory(UploadFileModel, form=UploadFileForm, extra=10)

	if request.method == 'POST':
		member: Member = Member.objects.get(id_member=request.POST['id_member'])
		image_title: str = os.path.splitext(str(request.FILES['image']))[0]
		form = MemberUploadFileForm({'image_title': image_title}, request.FILES, instance=member)
		if form.is_valid():
			# file is saved
			form.save()
		content = {
			"message": "파일 업로드 완료",
			"result": {"image_title": member.image_title}
		}
		return Response(content, status=status.HTTP_200_OK)

	elif request.method == 'DELETE':
		data = request.body.decode('utf-8')
		received_json_data = json.loads(data)
		id_member = received_json_data['id_member']
		try:
			q = Member.objects.get(id_member=id_member)
		except Member.DoesNotExist:
			content = {
				"message": "회원 프로필 사진이 없습니다.",
				"result": {"id_member": id_member}
			}
			return Response(content, status=status.HTTP_404_NOT_FOUND)

		q.delete_image()
		content = {
			"message": "삭제 완료",
			"result": {"id_member": q.id_member}
		}
		return Response(content, status=status.HTTP_204_NO_CONTENT)
