from django.db import models

from common.models.rate_model import Rate
from common.models.shopper_review_model import ShopperReview


class ShopperRate(models.Model):
	id_review_shopper: ShopperReview = models.ForeignKey('common.ShopperReview', models.DO_NOTHING,
	                                                     db_column='id_review_shopper')
	id_rate: Rate = models.ForeignKey('common.Rate', models.DO_NOTHING, db_column='id_rate')

	class Meta:
		db_table = 'shopper_rate'
