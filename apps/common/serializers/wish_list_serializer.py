from rest_framework import serializers

from common.models.wishlist_model import Wishlist


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ('id_wishlist', 'id_product', 'id_member', 'cdate')
