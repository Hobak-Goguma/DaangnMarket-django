from django.db import models

from common.models.member_model import Member
from common.models.seller_review_model import SellerReview
from posts.models.product_model import Product


class RealDeal(models.Model):
	id_real_deal: int = models.AutoField(primary_key=True)
	id_review_seller: SellerReview = models.ForeignKey('common.SellerReview', models.DO_NOTHING,
	                                                   db_column='id_review_seller')
	id_shopper: Member = models.ForeignKey('common.Member', models.DO_NOTHING, db_column='id_shopper')
	id_product: Product = models.ForeignKey('posts.Product', models.DO_NOTHING, db_column='id_product')

	class Meta:
		db_table = 'real_deal'
		app_label = 'common'
