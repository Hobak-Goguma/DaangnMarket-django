import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from common.models.rate_model import Rate
from common.models.realdeal_model import RealDeal
from common.models.shopper_rate_model import ShopperRate
from common.models.shopper_review_model import ShopperReview
from common.serializers.real_deal_serializer import ShopperReviewSerializer


@api_view(['GET','POST'])
def shopper_review(request):
    """
    구매자의 리뷰를 봅니다(구매자 -> 판매자)
    """
    if request.method == 'GET':
        shopperreview = ShopperReview.objects.all()
        serializer = ShopperReviewSerializer(shopperreview, many=True)
        return Response(serializer.data)
    #POST일 경우
    Data = json.loads(request.body)
    try :
        id_real_deal = RealDeal.objects.get(id_product = Data['id_product'])
    except RealDeal.DoesNotExist:
        if not(request.body) :
            content =   {
                "message" : "rate, id_product 필드는 필수입니다.",
                "result" : {}
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
#TODO content 메세지 메소드 리팩토링, api별 필수 파라미터가 없는 경우에 대한 Response 를 메소드 처리 해야합니다 *^^*
        essential_fields = ['id_product', 'rate', 'content']
        for essential_field in essential_fields :
            if not(Data.get(essential_field)):
                content =   {
                "message" : essential_field + " 필드는 필수입니다.",
                "result" : {}
                }
                return Response(content, status=status.HTTP_400_BAD_REQUEST)

        # if not(Data.get('id_product')) :
        #     content =   {
        #         "message" : "id_product 필드는 필수입니다.",
        #         "result" : {}
        #     }
        #     return Response(content, status=status.HTTP_400_BAD_REQUEST)
        # if not(Data.get('rate')) :
        #     content =   {
        #         "message" : "rate 필드는 필수입니다.",
        #         "result" : {}
        #     }
        #     return Response(content, status=status.HTTP_400_BAD_REQUEST)
        # if not(Data.get('content')) :
        #     content = {
        #         "message" : "content 필드는 필수입니다.",
        #         "result" : {}
        #     }
        #     return Response(content, status=status.HTTP_400_BAD_REQUEST)

        #seller review 저장
        id_real_deal = RealDeal.objects.get(id_product = Data.get('id_product'))
        review = ShopperReview.objects.create(id_real_deal = id_real_deal, content = Data.get('content'))
        review = int(review.id_review_shopper)
        temp_review = ShopperReview.objects.get(id_review_shopper=review)
        #rate 저장
        rate = Data['rate'].split(',')
        for i in rate:
            temp_rate = Rate.objects.get(id_rate=i)
            ShopperRate.objects.create(id_review_shopper = temp_review, id_rate =temp_rate)
        shopperreview = ShopperReview.objects.get(id_review_shopper = review)
        serializer = ShopperReviewSerializer(shopperreview)
        content = {
                    "message" : "후기등록 완료",
                    "result"  : {
                                    "review" : serializer.data,
                                    "rate" : rate
                                }
        }
        return Response(content, status=status.HTTP_201_CREATED)
    content = {
            "message" : "이미 후기가 등록된 상품입니다.",
            "result" : {}
    }
    return Response(content, status=status.HTTP_400_BAD_REQUEST)