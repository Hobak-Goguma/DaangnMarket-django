from common.models.shopper_review_model import ShopperReview
from common.serializers.real_deal_serializer import ShopperReviewSerializer


# 특정 실거래의 구매자 리뷰
def shopper_review_list(id_real_deal):
    shopperreview = ShopperReview.objects.filter(id_real_deal=id_real_deal)
    serializer = ShopperReviewSerializer(shopperreview, many=True)
    return serializer.data
