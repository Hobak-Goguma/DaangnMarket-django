from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

# from common.serializers.serializers import
from common.models.member_addr_model import Memberaddr
from common.models.nearby_Location_model import NearbyLocation
from posts.models.company_model import Company
from posts.serializers.company_serializer import CompanySearchSerializer


@api_view(['GET'])
def location_search_company(request):
	"""
	사용자의 위치에 따른 company 검색

	---
	# 내용
		- q = 검색어
		- page = 현재 페이지
		- page_size = 한번에 뿌려주는 상품 갯수
	# Header
		- id-member : header에 id_member를 캐치해서 선택된 addr, dis를 활용한다.
		* header에 id-member값이 없을경우, 비회원 전체검색 로직
	"""
	paginator = PageNumberPagination()

	paginator.page_size_query_param = "page_size"
	Search = request.GET['q']

	# 회원 검색
	if 'id-member' in request.headers:
		try:
			member_addr = Memberaddr.objects.filter(id_member=request.headers['id-member']).get(select='Y')
			addr = member_addr.addr
			dis = member_addr.distance
		except Memberaddr.DoesNotExist:
			content = {
				"message": "설정된 주소가 없습니다. 주소를 설정해 주세요.",
				"result": {}
			}
			return Response(content, status=status.HTTP_204_NO_CONTENT)

		location = NearbyLocation.objects.filter(dong=addr).filter(distance=dis)
		company_sum = Company.objects.filter(name__contains=Search).filter(addr=addr)
		for i in location:
			company = Company.objects.filter(name__contains=Search).filter(addr=i.nearby_dong)
			company_sum = company_sum | company
		if company_sum.count() == 0:
			content = {
				"message": "검색한 업체가 없습니다.",
				"result": {"입력한 검색어": Search}
			}
			return Response(content, status=status.HTTP_204_NO_CONTENT)

		paginated_company_sum = paginator.paginate_queryset(company_sum, request)

		if paginated_company_sum is not None:
			serializers = CompanySearchSerializer(paginated_company_sum, many=True)
			return paginator.get_paginated_response(serializers.data)

		serializer = CompanySearchSerializer(company_sum, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	# 비회원
	else:
		company = Company.objects.filter(name__contains=Search)
		if company.count() == 0:
			content = {
				"message": "검색한 없체가 없습니다.",
				"result": {"입력한 검색어": Search}
			}
			return Response(content, status=status.HTTP_204_NO_CONTENT)
		paginated_company = paginator.paginate_queryset(company, request)
		if paginated_company is not None:
			serializers = CompanySearchSerializer(paginated_company, many=True)
			return paginator.get_paginated_response(serializers.data)

		serializer = CompanySearchSerializer(company, many=True)

		return Response(serializer.data, status=status.HTTP_200_OK)
