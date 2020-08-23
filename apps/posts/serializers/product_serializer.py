from rest_framework import serializers
from sorl.thumbnail import get_thumbnail

from posts.models.product_model import Product
from posts.models.posts_product_image_model import ProductImage


class ProductSerializer(serializers.ModelSerializer):
    # id_member_id = serializers.IntegerField(source='id_member')
    # member = serializers.ForeignKey(Member, models.CASCADE, related_name='member_id')
    class Meta:
        model = Product
        fields = ('id_product', 'id_member', 'name', 'price', 'info', 'code', 'views', 'state', 'addr')


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image',)


class ProductSearchSerializer(serializers.ModelSerializer):
    # thum = serializers.SerializerMethodField()
    thum_first = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id_product', 'id_member', 'name', 'price', 'info', 'code', 'views', 'state', 'addr', 'thum_first')

    # def get_thum_first(self, obj):
    #     k = ProductImage.objects.filter(id_product = obj.id_product).first()
    #     k2 = ProductImageSerializer(k).data
    #     if k2['image']:
    #         k2 = 'http://127.0.0.1:8000' + '/image' + str(k2['image'])
    #     return k2

    def get_thum_first(self, obj):
        Data = ProductImageSerializer(obj.thum.first()).data
        if Data['image']:
            # print('------------------BASE_DIR', settings.MEDIA_URL)
            # print('-----------object', obj.thum.first())
            # print()
            # _PATH = os.path.join(settings.BASE_DIR, str(obj.thum.first()))
            # print(obj.thum)
            # print(_PATH)
            # print(settings.BASE_DIR + str(obj.thum.first()))
            Data['image'] = 'http://www.daangn.site/image' + get_thumbnail(obj.thum.first().image, '1500x1500',
                                                                           crop='center', quality=82).url
        # request.META['HTTP_HOST']+
        # self.context['request'].META.get('HTTP_HOST')
        return Data

    # def get_thum(self, obj):
    #     return  ProductImageSerializer(obj.thum.first()).data


class ProductTouchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id_product', 'id_member', 'name', 'price', 'info', 'code', 'views', 'state', 'addr')
        read_only_fields = ['id_product', 'id_member', 'views', 'state']
