from datetime import datetime

from django.db import models

from common.models.member_model import Member


class SellerReview(models.Model):
	id_review_seller: int = models.AutoField(primary_key=True)
	id_seller: Member = models.ForeignKey('common.Member', models.DO_NOTHING, db_column='id_seller')
	content: str = models.CharField(max_length=100)
	cdate: datetime = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'seller_review'
