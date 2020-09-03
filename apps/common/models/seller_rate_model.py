from django.db import models

from common.models.rate_model import Rate
from common.models.seller_review_model import SellerReview


class SellerRate(models.Model):
	id_review_seller: SellerReview = models.ForeignKey('common.SellerReview', models.DO_NOTHING,
	                                                   db_column='id_review_seller')
	id_rate: Rate = models.ForeignKey('common.Rate', models.DO_NOTHING, db_column='id_rate')

	class Meta:
		db_table = 'seller_rate'
