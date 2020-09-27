from rest_framework import serializers
from sorl.thumbnail import get_thumbnail

from posts.models.company_image_model import CompanyImage
from posts.models.company_model import Company
from posts.models.posts_category_code_model import CategoryCode


class CompanyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyImage
        fields = ('image',)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id_company', 'id_member', 'name', 'addr', 'tel', 'info', 'code', 'views')
        read_only_fields = ['__all__']

    def validate_code(self, value):
        """
		check that the code is about local shop
		"""
        if value.code != CategoryCode.CODE.LOCAL_SHOP.value:
            raise serializers.ValidationError("올바른 code값이 아닙니다.")
        return value


class CompanyTouchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id_company', 'id_member', 'name', 'addr', 'tel', 'info', 'code')
        read_only_fields = ['id_member', 'id_company']


class CompanySearchSerializer(serializers.ModelSerializer):
    thum = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = ('id_company', 'id_member', 'name', 'addr', 'tel', 'info', 'code', 'views', 'thum')
        read_only_fields = ['__all__']

    def get_thum(self, obj):
        Data = CompanyImageSerializer(obj.thum.first()).data
        if Data['image']:
            Data['image'] = self.context['request'].META['HTTP_HOST'] + '/posts' + get_thumbnail(
                obj.thum.first().image, '1500x1500',
                crop='center', quality=82).url
        return Data
