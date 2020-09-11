import os

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from common.forms.member_upload_file_form import MemberUploadFileForm
from common.models.member_model import Member
from common.views.schema.member_upload_file_schema import member_upload_file_delete, member_upload_file_parameter


@swagger_auto_schema(method='post',
                     manual_parameters=member_upload_file_parameter,
					 responses={
					 	201: 'File Upload Successful.'
					 })
@swagger_auto_schema(method='delete',
                     manual_parameters=member_upload_file_delete,
					 responses={
					 	204: 'File Deleted Successful.'
					 })
@api_view(('post', 'delete'))
@parser_classes([FormParser, MultiPartParser])
def member_upload_file(request):
	"""
	Product 사진 업로드 API

	---
	image_title은 파일의 원본 이름이 저장됌.
	"""
	# 이미지 업로드 제한갯수 최대 10개 (try)
	# ImageFormSet = modelformset_factory(UploadFileModel, form=UploadFileForm, extra=10)

	if request.method == 'POST':
		id_member = request.POST['id_member']
		member: Member = Member.objects.get(id_member=id_member)
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
		id_member = request.POST['id_member']
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
