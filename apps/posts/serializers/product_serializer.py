from rest_framework import serializers
from sorl.thumbnail import get_thumbnail

from posts.models.posts_product_image_model import ProductImage
from posts.models.product_model import Product


class ProductSerializer(serializers.ModelSerializer):
	# id_member_id = serializers.IntegerField(source='id_member')
	# member = serializers.ForeignKey(Member, models.CASCADE, related_name='member_id')
	class Meta:
		model = Product
		fields = ('id_product', 'id_member', 'name', 'price', 'info', 'code', 'views', 'state', 'addr')
		read_only_fields = ['__all__']

class ProductImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProductImage
		fields = ('image',)


class ProductSearchSerializer(serializers.ModelSerializer):
	thum = serializers.SerializerMethodField()

	class Meta:
		model = Product
		fields = (
			'id_product', 'id_member', 'name', 'price', 'info', 'code', 'views', 'state', 'addr', 'thum', 'cdate')

	def get_thum(self, obj):
		Data = ProductImageSerializer(obj.thum.first()).data
		if Data['image']:
			Data['image'] = self.context['request'].META['HTTP_HOST'] + '/posts' + get_thumbnail(
				obj.thum.first().image, '1500x1500',
				crop='center', quality=82).url
		return Data


class ProductTouchSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('id_product', 'id_member', 'name', 'price', 'info', 'code', 'views', 'state', 'addr')
		read_only_fields = ['id_product', 'id_member', 'views', 'state']
