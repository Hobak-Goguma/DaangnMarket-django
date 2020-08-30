from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.utils import json

from posts.forms.product_upload_file_forms import ProductUploadFileForm
from posts.models.posts_product_image_model import ProductImage


@api_view(('POST', 'DELETE'))
def product_upload_file(request):
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
		form = ProductUploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			# file is saved
			form.save()
			return Response(status=status.HTTP_200_OK)

		else:
			content = {
				"message": "데이터 형식이 맞지 않습니다.",
			}
			return Response(content, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		data = request.body.decode('utf-8')
		received_json_data = json.loads(data)
		Title = received_json_data['title']
		q = ProductImage.objects.get(title=Title)
		q.delete()
		content = {
			"message": "삭제 완료",
			"result": {"title": Title}
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
