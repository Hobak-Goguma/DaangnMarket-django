from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from common.serializers.company_serializer import CompanySerializer, CompanyTouchSerializer
from posts.models.company_model import Company


@api_view(['GET', 'PUT', 'DELETE'])
def company_detail(request, id_company):
    """
    특정 업체리스트를 조회, 수정, 삭제 합니다.
    """
    try:
        company = Company.objects.get(pk=id_company)
    except Company.DoesNotExist:
        content = {
            "message" : "없는 업체 입니다.",
            "result" : {}
                }
        return Response(content, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CompanyTouchSerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        company.delete()
        content = {
            "message" : "pk :" + id_company + " 삭제 완료",
            "result" : {}
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)