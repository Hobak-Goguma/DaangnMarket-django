from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
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
		member = Member.objects.get(id_member=request.POST['id_member'])
		form = MemberUploadFileForm(request.POST, request.FILES, instance=member)
		if form.is_valid():
			# file is saved
			form.save()
			return Response(status=status.HTTP_200_OK)

	elif request.method == 'DELETE':
		data = request.body.decode('utf-8')
		received_json_data = json.loads(data)
		title = received_json_data['image_title']
		q = Member.objects.get(title=title)
		q.delete_image()
		content = {
			"message": "삭제 완료",
			"result": {"title": title}
		}
		return Response(content, status=status.HTTP_204_NO_CONTENT)
