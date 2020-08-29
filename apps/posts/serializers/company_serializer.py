from rest_framework import serializers

from posts.models.company_model import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id_company', 'id_member', 'name', 'addr', 'tel', 'info', 'category', 'img')


class CompanyTouchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id_company', 'id_member', 'name', 'addr', 'tel', 'info', 'category', 'img')
        read_only_fields = ['id_member']

class CompanySearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id_company', 'id_member', 'name', 'addr', 'tel', 'info', 'code', 'img')
        read_only_fields =  '__all__'