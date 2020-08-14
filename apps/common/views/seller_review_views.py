import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from common.models.member_model import Member
from posts.models.product_model import Product
from common.models.rate_model import Rate
from common.models.realdeal_model import RealDeal
from common.models.seller_rate_model import SellerRate
from common.models.seller_review_model import SellerReview
from common.serializers.real_deal_serializer import SellerReviewSerializer


@api_view(['GET','POST'])
def seller_review(request):
    """
    판매자의 리뷰를 봅니다(판매자 -> 구매자)
    """
    if request.method == 'GET':
        sellerreview = SellerReview.objects.all()
        serializer = SellerReviewSerializer(sellerreview, many=True)
        return Response(serializer.data)

    #POST일 경우
    Data = json.loads(request.body)
    try :
        id_real_deal = RealDeal.objects.get(id_product = Data['id_product'])
    except RealDeal.DoesNotExist:
        if request.body :
            #json 확인
            essential_fields = ['id_shopper', 'id_product', 'rate']
            for essential_field in essential_fields :
                if not(Data.get(essential_field)):
                    content =   {
                            "message" : essential_field + " 필드는 필수입니다.",
                            "result" : {}
                                }
                    return Response(content, status=status.HTTP_400_BAD_REQUEST)
            serializer = SellerReviewSerializer(data=request.data)
            if serializer.is_valid():
                #seller review 저장
                serializer.save()
                shopper = Data['id_shopper']
                review = int(serializer.data['id_review_seller'])
                product = Data['id_product']
                temp_shopper = Member.objects.get(id_member=shopper)
                temp_review = SellerReview.objects.get(id_review_seller=review)
                temp_product = Product.objects.get(id_product = product)
                #realdeal 저장
                RealDeal.objects.create(id_shopper = temp_shopper, id_review_seller = temp_review,id_product = temp_product)
                #rate 저장
                rate = Data['rate'].split(',')
                for i in rate:
                    temp_rate = Rate.objects.get(id_rate=i)
                    SellerRate.objects.create(id_review_seller = temp_review, id_rate =temp_rate)
                content = {
                            "message" : "후기등록 완료",
                            "result"  : {
                                            "review" : serializer.data,
                                            "rate" : rate,
                                            "id_shopper" : shopper,
                                            "id_product" : product
                                        }
                        }
                return Response(content, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    content = {
                "message" : "이미 후기가 등록된 상품입니다.",
                "result" : {}
                    }
    return Response(content, status=status.HTTP_400_BAD_REQUEST)