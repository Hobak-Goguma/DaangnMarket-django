from datetime import datetime

from django.db import models

from common.models.member_model import Member
from posts.models.posts_category_code_models import CategoryCode


class Product(models.Model):
	class STATE(models.TextChoices):
		ON_SALE = 'SALE', '판매중'
		BOOKING = 'BOOKING', '예약중'
		COMPLETED = 'COMPLETED', '거래완료'
		HIDE = 'HIDE', '숨기기'

	id_product: int = models.AutoField(primary_key=True)
	id_member: int = models.ForeignKey('common.Member', on_delete=models.CASCADE, db_column='id_member',
	                                   related_name='product_member')
	name: str = models.CharField(max_length=100)
	price: int = models.IntegerField(default=0)
	info: str = models.CharField(max_length=3000)
	code: CategoryCode = models.ForeignKey('posts.CategoryCode', on_delete=models.DO_NOTHING, db_column='code',
	                                       related_name='product_code', default=CategoryCode.CODE.ETC)
	views: int = models.IntegerField(default=0)
	state: STATE = models.CharField(max_length=10, choices=STATE.choices, default=STATE.ON_SALE)
	addr: str = models.CharField(max_length=200)
	cdate: datetime = models.DateTimeField(auto_now_add=True)
	udate: datetime = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'product'

	class ProductManager(models.Manager):
		def create_product(self, id_member, name, price, info, code, addr):
			id_member = Member.objects.get(id_member=id_member)
			code = CategoryCode.objects.get(code=code)
			product = self.create(id_member=id_member, name=name, price=price, info=info, code=code, addr=addr)
			return product

	objects = ProductManager()
