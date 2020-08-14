from rest_framework import serializers

from common.models.realdeal_model import RealDeal
from common.models.seller_rate_model import SellerRate
from common.models.seller_review_model import SellerReview
from common.models.shopper_rate_model import ShopperRate
from common.models.shopper_review_model import ShopperReview
from posts.serializers.product_serializer import ProductSerializer


class RealDealSerializer(serializers.ModelSerializer):
    id_product = ProductSerializer(read_only=True)

    class Meta:
        model = RealDeal
        fields = ('id_real_deal', 'id_review_seller', 'id_shopper', 'id_product')


class SellerRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerRate
        fields = ('id_review_seller', 'id_rate')


class ShopperRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopperRate
        fields = ('id_review_shopper', 'id_rate')


class SellerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerReview
        fields = ('id_review_seller', 'id_seller', 'content', 'cdate')


class ShopperReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopperReview
        fields = ('id_review_shopper', 'id_real_deal', 'content', 'cdate')
