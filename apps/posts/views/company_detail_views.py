from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sorl.thumbnail import get_thumbnail

from posts.models.company_image_model import CompanyImage
from posts.models.company_model import Company
from posts.serializers.company_serializer import CompanySerializer, CompanyTouchSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def company_detail(request, id_company):
	"""
	특정 업체리스트를 조회, 수정, 삭제 합니다.

	---
	# parameter
		- s = 사진픽셀 크기 ex) 400x400
	# 내용
		image : {
		- thum : 사진 썸네일
		- origin : 사진 원본
		}
	"""
	try:
		company = Company.objects.get(id_company=id_company)
	except Company.DoesNotExist:
		content = {
			"message": "없는 업체 입니다.",
			"result": {}
		}
		return Response(content, status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		company.views += 1
		company.save()
		serializer = CompanySerializer(company)

		s = request.GET['s']
		image = CompanyImage.objects.filter(id_company=id_company).order_by('id')
		imageList = []
		data = serializer.data
		print(image.count())
		print(image[0].image)
		for i in range(image.count()):
			imageDict = {}
			imageDict['thum'] = request.META['HTTP_HOST'] + '/posts' + get_thumbnail(image[i].image, s, crop='center',
			                                                                         quality=82).url
			imageDict['origin'] = request.META['HTTP_HOST'] + '/posts/media/' + str(image[i].image)
			imageList.append(imageDict)
		data['image'] = imageList
		return Response(data, status=status.HTTP_200_OK)

	elif request.method == 'PUT':
		serializer = CompanyTouchSerializer(company, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		company.delete()
		content = {
			"message": "pk :" + id_company + " 삭제 완료",
			"result": {}
		}
		return Response(content, status=status.HTTP_204_NO_CONTENT)
