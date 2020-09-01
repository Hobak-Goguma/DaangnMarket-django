from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from posts.models.company_model import Company
from posts.serializers.company_serializer import CompanySerializer


@api_view(['GET', 'POST'])
def company_list(request):
	"""
	업체리스트를 모두 보여주거나 새 업체리스트를 만듭니다.
	"""
	if request.method == 'GET':
		company = Company.objects.all()
		serializer = CompanySerializer(company, many=True, context={'request': request})
		return Response(serializer.data, status=status.HTTP_200_OK)

	elif request.method == 'POST':
		serializer = CompanySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
