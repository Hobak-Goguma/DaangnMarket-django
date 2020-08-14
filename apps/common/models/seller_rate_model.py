from django.db import models


class SellerRate(models.Model):
    id_review_seller = models.ForeignKey('common.SellerReview', models.DO_NOTHING, db_column='id_review_seller')
    id_rate = models.ForeignKey('common.Rate', models.DO_NOTHING, db_column='id_rate')

    class Meta:
        db_table = 'seller_rate'
        app_label = 'common'