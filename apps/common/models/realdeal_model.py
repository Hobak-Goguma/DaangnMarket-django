from django.db import models


class RealDeal(models.Model):
    id_real_deal = models.AutoField(primary_key=True)
    id_review_seller = models.ForeignKey('common.SellerReview', models.DO_NOTHING, db_column='id_review_seller')
    id_shopper = models.ForeignKey('common.Member', models.DO_NOTHING, db_column='id_shopper')
    id_product = models.ForeignKey('common.Product', models.DO_NOTHING, db_column='id_product')

    class Meta:
        db_table = 'real_deal'
        app_label = 'common'