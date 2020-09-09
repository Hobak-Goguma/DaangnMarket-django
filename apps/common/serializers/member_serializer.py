from django.utils import timezone
from rest_framework import serializers
from sorl.thumbnail import get_thumbnail

from common.models.member_addr_model import Memberaddr
from common.models.member_model import Member


class MemberSerializer(serializers.ModelSerializer):
	udate = serializers.DateTimeField(default=timezone.now)
	last_date = serializers.DateTimeField(default=timezone.now)
	image = serializers.SerializerMethodField()

	class Meta:
		model = Member
		fields = (
			'id_member', 'name', 'nick_name', 'user_id', 'user_pw', 'tel', 'birth', 'email', 'gender', 'image', 'cdate',
			'udate', 'last_date')

	def get_image(self, obj):
		Data = None
		if obj.image:
			Data = self.context['request'].META['HTTP_HOST'] + get_thumbnail(
				obj.image, '800x800',
				crop='center', quality=82).url
		return Data


class MemberReviseSerializer(serializers.ModelSerializer):
	udate = serializers.DateTimeField(default=timezone.now)

	class Meta:
		model = Member
		fields = ('id_member', 'user_pw', 'udate')


class MemberTouchSerializer(serializers.ModelSerializer):
	udate = serializers.DateTimeField(default=timezone.now)

	class Meta:
		model = Member
		fields = ('nick_name', 'tel', 'birth', 'email', 'gender', 'udate',)
		read_only_fields = ['id_member', ]


class memberAddrSerializer(serializers.ModelSerializer):
	class Meta:
		model = Memberaddr
		fields = ('id_member', 'addr', 'distance', 'select')
# read_only_fields = ['user_id']

# class MemberSerializer(serializers.Serializer):
#     id_member = serializers.AutoField(primary_key=True)
#     name = serializers.CharField(max_length=30)
#     nick_name = serializers.CharField(max_length=30)
#     user_id = serializers.CharField(max_length=30)
#     user_pw = serializers.CharField(max_length=55)
#     tel = serializers.CharField(max_length=20)
#     birth = serializers.DateField()
#     email = serializers.CharField(max_length=30)
#     gender = serializers.CharField(max_length=6)
#     add = serializers.CharField(max_length=200)
#     cdate = serializers.DateTimeField()
#     udate = serializers.DateTimeField()
#     last_date = serializers.DateTimeField()

#     def create(self, validated_data):
#         """
#         검증한 데이터로 새 `Member` 인스턴스를 생성하여 리턴합니다.
#         """
#         return Member.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         검증한 데이터로 기존 `Member` 인스턴스를 업데이트한 후 리턴합니다.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance
