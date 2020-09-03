from datetime import datetime

from django.db import models

from common.models.realdeal_model import RealDeal


class ShopperReview(models.Model):
	id_review_shopper: int = models.AutoField(primary_key=True)
	id_real_deal: RealDeal = models.ForeignKey('common.RealDeal', models.DO_NOTHING, db_column='id_real_deal')
	content: str = models.CharField(max_length=100)
	cdate: datetime = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'shopper_review'
