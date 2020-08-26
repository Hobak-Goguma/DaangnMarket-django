from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

# from common.serializers.serializers import
from common.models.member_addr_model import Memberaddr
from common.models.nearby_Location_model import NearbyLocation
from posts.models.product_model import Product
from posts.serializers.product_serializer import ProductSearchSerializer


@api_view(['GET'])
def location_search(request):
    """
    사용자의 위치에 따른 product 검색

    ---
    # 내용
        - q = 검색어
        - page = 현재 페이지
        - page_size = 한번에 뿌려주는 상품 갯수
    # Header
        - id-member : header에 id_member를 캐치해서 선택된 addr, dis를 활용한다.
        * header에 id-member값이 없을경우, 비회원 전체검색 로직
    """
    # 디폴트 페이지네이션 사용
    paginator = PageNumberPagination()

    # 페이지 사이즈를 page_size라는 이름의 파라미터로 받을 거임
    paginator.page_size_query_param = "page_size"
    Search = request.GET['q']

    #회원 검색
    if 'id-member' in request.headers :
        #주소 유무 체크
        try :
            memberaddr = Memberaddr.objects.filter(id_member = request.headers['id-member']).get(select = 'Y')
            addr =  memberaddr.addr
            dis = memberaddr.distance
        #설정된 주소가 없을
        except Memberaddr.DoesNotExist :
            content = {
                "message" : "설정된 주소가 없습니다. 주소를 설정해 주세요.",
                "result" : {}
                    }
            return Response(content,status=status.HTTP_204_NO_CONTENT)


            # product = Product.objects.filter(name__contains = Search)
            # if product.count() == 0 :
            #     content = {
            #     "message" : "검색한 제품이 없습니다.",
            #     "result" : {"입력한 검색어" : Search}
            #         }
            #     return Response(content,status=status.HTTP_204_NO_CONTENT)
            # serializer = ProductSearchSerializer(product, many=True)
            # # 페이지 적용된 쿼리셋
            # paginated_product = paginator.paginate_queryset(product, request)
            # # 페이지 파라미터 (page, page_size) 있을 경우
            # # page_size 만 있을 경우 page=1 처럼 동작함
            # # page만 있을 경우 아래 if문 안 탐
            # if paginated_product is not None:
            #     serializers = ProductSearchSerializer(paginated_product, many=True)
            #     return paginator.get_paginated_response(serializers.data)

            # # # 페이지 파라미터 없을 경우
            # serializer = ProductSearchSerializer(product, many =True)
            # return Response(serializer.data)

        #근처 주소 검색
        location = NearbyLocation.objects.filter(dong = addr).filter(distance = dis)
        product_sum = Product.objects.filter(name__contains = Search).filter(addr = addr)
        for i in location :
            product = Product.objects.filter(name__contains = Search).filter(addr = i.nearby_dong)
            product_sum = product_sum | product
        if product_sum.count() == 0 :
            content = {
                "message" : "검색한 제품이 없습니다.",
                "result" : {"입력한 검색어" : Search}
                    }
            return Response(content,status=status.HTTP_204_NO_CONTENT)
        # 페이지 적용된 쿼리셋
        paginated_product_sum = paginator.paginate_queryset(product_sum, request)
        # 페이지 파라미터 (page, page_size) 있을 경우
        # page_size 만 있을 경우 page=1 처럼 동작함
        # page만 있을 경우 아래 if문 안 탐
        if paginated_product_sum is not None:
            serializers = ProductSearchSerializer(paginated_product_sum, many=True)
            return paginator.get_paginated_response(serializers.data)

        # # 페이지 파라미터 없을 경우
        serializer = ProductSearchSerializer(product_sum, many =True)
        return Response(serializer.data)
    #비회원
    else :
        #모든 제품 검색
        product = Product.objects.filter(name__contains = Search)
        if product.count() == 0 :
            content = {
            "message" : "검색한 제품이 없습니다.",
            "result" : {"입력한 검색어" : Search}
                }
            return Response(content,status=status.HTTP_204_NO_CONTENT)
        serializer = ProductSearchSerializer(product, many=True)
        # 페이지 적용된 쿼리셋
        paginated_product = paginator.paginate_queryset(product, request)
        # 페이지 파라미터 (page, page_size) 있을 경우
        # page_size 만 있을 경우 page=1 처럼 동작함
        # page만 있을 경우 아래 if문 안 탐
        if paginated_product is not None:
            serializers = ProductSearchSerializer(paginated_product, many=True)
            return paginator.get_paginated_response(serializers.data)

        # # 페이지 파라미터 없을 경우
        serializer = ProductSearchSerializer(product, many =True)

        return Response(serializer.data)